import {defineStore} from 'pinia'
import {ref, computed} from 'vue'
import {MessageEntity} from '../entities/MessageEntity'
import {ChatResponseEntity} from '../entities/ChatResponseEntity'
import {useWebSocketConnection} from '../composables/useWebSocketConnection'
import {TaskQueue} from "../utils/TaskQueue.js";

export const useChatStore = defineStore('chat', () => {
  const q = new TaskQueue(0);
  const sessionId = ref(null)
  const messages = ref([])
  
  const wsConnection = useWebSocketConnection()
  
  const lastMessage = computed(() => {
    return messages.value[messages.value.length - 1] || null
  })
  
  const isLoading = computed(() => {
    return lastMessage.value && lastMessage.value.isLoading
  })
  
  
  const hasMessages = computed(() => messages.value.length > 0)
  
  const setLastMessage = (message) => {
    messages.value[messages.value.length - 1] = {...lastMessage.value, ...message}
  }
  const handleSessionId = (id) => {
    sessionId.value = id
  }
  
  
  const handleToken = (data) => {
    q.push(() => {
      setLastMessage({
        isLoading: false,
        content: lastMessage.value.content += data.content,
        sources: data.sources,
      })
    })
  }
  
  const handleMessage = (data) => {
    if (lastMessage.value?.isLoading) {
      const response = ChatResponseEntity.create(data)
      
      setLastMessage({
        isLoading: false,
        sources: response.sources,
      })
      
      
      if (response.sessionId) {
        sessionId.value = response.sessionId
      }
    }
  }
  
  const handleError = (errorData) => {
    if (lastMessage.value?.isLoading) {
      setLastMessage({
        isLoading: false,
        error: errorData.message,
      })
    }
  }
  
  const connect = async () => {
    await wsConnection.connect({
      onSessionId: handleSessionId,
      onToken: handleToken,
      onMessage: handleMessage,
      onError: handleError,
    })
  }
  
  
  const sendMessage = (content) => {
    if (!content.trim() || !wsConnection.isConnected.value) return
    
    const userMessage = MessageEntity.createUserMessage(content)
    messages.value.push(userMessage)
    
    const loadingMessage = MessageEntity.createLoadingMessage()
    messages.value.push(loadingMessage)
    
    try {
      wsConnection.sendMessage(content)
    } catch (err) {
      loadingMessage.error = err.message
      loadingMessage.isLoading = false
    }
  }
  
  const reset = () => {
    messages.value = []
    wsConnection.error.value = null
    
    if (wsConnection.isConnected.value) {
      disconnect()
      connect()
    }
  }
  
  const disconnect = () => {
    wsConnection.disconnect()
  }
  
  return {
    sessionId,
    messages,
    isConnecting: wsConnection.isConnecting,
    isConnected: wsConnection.isConnected,
    error: wsConnection.error,
    lastMessage,
    isLoading,
    hasMessages,
    connect,
    sendMessage,
    reset,
    disconnect,
  }
})
