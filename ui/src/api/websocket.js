export const WebSocketState = {
  CONNECTING: 0,
  OPEN: 1,
  CLOSING: 2,
  CLOSED: 3
}

export const MessageType = {
  SESSION: 'session',
  END: 'end',
  ERROR: 'error'
}

export class WebSocketClient {
  #ws = null
  #reconnectAttempts = 0
  #isManualDisconnect = false
  #reconnectTimeout = null
  #eventHandlers = new Map()

  constructor(config = {}) {
    this.maxReconnectAttempts = config.maxReconnectAttempts ?? 5
    this.reconnectDelay = config.reconnectDelay ?? 2000
    this.url = config.url
  }

  connect() {
    this.#isManualDisconnect = false

    return new Promise((resolve, reject) => {
      if (this.#ws?.readyState === WebSocketState.OPEN) {
        resolve()
        return
      }

      try {
        const wsUrl = this.url || `${import.meta.env.VITE_WS_URL}/api/ws/chat`
        this.#ws = new WebSocket(wsUrl)

        this.#ws.onopen = () => {
          this.#reconnectAttempts = 0
          this.#emit('open')
          resolve()
        }

        this.#ws.onmessage = (event) => {
          try {
            const data = JSON.parse(event.data)
            this.#handleMessage(data)
          } catch (error) {
            this.#emit('error', {
              message: 'Помилка обробки повідомлення від сервера',
              error
            })
          }
        }

        this.#ws.onerror = (error) => {
          const errorMessage = this.#reconnectAttempts > 0
            ? `Помилка підключення (спроба ${this.#reconnectAttempts}/${this.maxReconnectAttempts})`
            : 'Помилка з\'єднання з сервером'

          this.#emit('error', { message: errorMessage, error })
          reject(error)
        }

        this.#ws.onclose = (event) => {
          this.#emit('close', event)

          if (!this.#isManualDisconnect && event.code !== 1000) {
            this.#scheduleReconnect()
          }
        }
      } catch (error) {
        this.#emit('error', {
          message: 'Не вдалося створити з\'єднання',
          error
        })
        reject(error)
      }
    })
  }

  #handleMessage(data) {
    const { type } = data

    switch (type) {
      case MessageType.SESSION:
        this.#emit('session', data.session_id)
        break

      case MessageType.END:
        this.#emit('message', {
          content: data.content,
          sources: data.sources || [],
          sessionId: data.session_id
        })
        break

      case MessageType.ERROR:
        this.#emit('error', {
          message: data.message || 'Помилка сервера',
          details: data
        })
        break

      default:
        this.#emit('unknown', data)
    }
  }

  send(message) {
    if (!this.#ws) {
      throw new Error('WebSocket не ініціалізовано')
    }

    const state = this.#ws.readyState

    if (state === WebSocketState.CONNECTING) {
      throw new Error('WebSocket ще підключається')
    }

    if (state === WebSocketState.CLOSING || state === WebSocketState.CLOSED) {
      throw new Error('WebSocket закрито')
    }

    if (state === WebSocketState.OPEN) {
      this.#ws.send(JSON.stringify({ message }))
    }
  }

  on(event, handler) {
    if (!this.#eventHandlers.has(event)) {
      this.#eventHandlers.set(event, new Set())
    }
    this.#eventHandlers.get(event).add(handler)
  }

  off(event, handler) {
    this.#eventHandlers.get(event)?.delete(handler)
  }

  #emit(event, data) {
    this.#eventHandlers.get(event)?.forEach(handler => {
      try {
        handler(data)
      } catch (error) {
        console.error(`Error in ${event} handler:`, error)
      }
    })
  }

  #scheduleReconnect() {
    if (this.#reconnectAttempts >= this.maxReconnectAttempts || this.#isManualDisconnect) {
      if (this.#reconnectAttempts >= this.maxReconnectAttempts) {
        this.#emit('error', {
          message: 'Не вдалося відновити з\'єднання після декількох спроб'
        })
      }
      return
    }

    this.#reconnectAttempts++

    this.#reconnectTimeout = setTimeout(() => {
      this.connect().catch(() => {})
    }, this.reconnectDelay)
  }

  disconnect() {
    this.#isManualDisconnect = true

    if (this.#reconnectTimeout) {
      clearTimeout(this.#reconnectTimeout)
      this.#reconnectTimeout = null
    }

    if (this.#ws) {
      this.#ws.close(1000, 'Client disconnect')
      this.#ws = null
    }

    this.#reconnectAttempts = 0
  }

  get isConnected() {
    return this.#ws?.readyState === WebSocketState.OPEN
  }

  get readyState() {
    return this.#ws?.readyState ?? WebSocketState.CLOSED
  }
}

export default new WebSocketClient()
