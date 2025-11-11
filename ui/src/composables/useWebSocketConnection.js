import { ref } from 'vue'
import websocket from '../api/websocket'

export function useWebSocketConnection() {
  const isConnecting = ref(false)
  const isConnected = ref(false)
  const error = ref(null)

  let eventHandlers = {
    onSessionId: null,
    onMessage: null,
    onError: null,
    onClose: null,
    onOpen: null,
  }

  const handleOpen = () => {
    isConnected.value = true
    eventHandlers.onOpen?.()
  }

  const handleClose = () => {
    isConnected.value = false
    eventHandlers.onClose?.()
  }

  const handleError = (errorData) => {
    error.value = errorData.message
    eventHandlers.onError?.(errorData)
  }

  const handleSessionId = (id) => {
    eventHandlers.onSessionId?.(id)
  }

  const handleMessage = (data) => {
    eventHandlers.onMessage?.(data)
  }

  const setupListeners = () => {
    websocket.on('session', handleSessionId)
    websocket.on('message', handleMessage)
    websocket.on('error', handleError)
    websocket.on('close', handleClose)
    websocket.on('open', handleOpen)
  }

  const removeListeners = () => {
    websocket.off('session', handleSessionId)
    websocket.off('message', handleMessage)
    websocket.off('error', handleError)
    websocket.off('close', handleClose)
    websocket.off('open', handleOpen)
  }

  const connect = async (handlers = {}) => {
    isConnecting.value = true
    error.value = null
    eventHandlers = { ...eventHandlers, ...handlers }

    try {
      setupListeners()
      await websocket.connect()
    } catch (err) {
      error.value = 'Не вдалося підключитися до сервера'
      isConnected.value = false
      throw err
    } finally {
      isConnecting.value = false
    }
  }

  const disconnect = () => {
    removeListeners()
    websocket.disconnect()
    isConnected.value = false
    eventHandlers = {
      onSessionId: null,
      onMessage: null,
      onError: null,
      onClose: null,
      onOpen: null,
    }
  }

  const sendMessage = (content) => {
    if (!content.trim() || !isConnected.value) {
      throw new Error('Неможливо відправити повідомлення')
    }

    try {
      websocket.send(content)
    } catch (err) {
      error.value = err.message
      throw err
    }
  }

  return {
    isConnecting,
    isConnected,
    error,
    connect,
    disconnect,
    sendMessage,
  }
}
