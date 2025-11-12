import {defineStore} from 'pinia'
import {ref, computed} from 'vue'
import {MessageEntity} from '../entities/MessageEntity'
import {ChatResponseEntity} from '../entities/ChatResponseEntity'
import {useWebSocketConnection} from '../composables/useWebSocketConnection'

export const useChatStore = defineStore('chat', () => {
  const sessionId = ref(null)
  const messages = ref([])
  const currentSources = ref([])
  
  const wsConnection = useWebSocketConnection()
  
  const lastMessage = computed(() => {
    return messages.value[messages.value.length - 1] || null
  })
  const isLoading = computed(() => {
    const last = lastMessage.value
    return last && last.isLoading
  })
  const hasMessages = computed(() => messages.value.length > 0)
  
  const handleSessionId = (id) => {
    sessionId.value = id
  }
  
  const handleMessage = (data) => {
    const lastMsg = lastMessage.value
    
    if (lastMsg?.isLoading) {
      const response = ChatResponseEntity.create(data)
      
      lastMsg.content = response.content
      lastMsg.sources = response.sources
      lastMsg.isLoading = false
      currentSources.value = response.sources
      
      if (response.sessionId) {
        sessionId.value = response.sessionId
      }
    }
  }
  
  const handleError = (errorData) => {
    const lastMsg = lastMessage.value
    
    if (lastMsg?.isLoading) {
      lastMsg.error = errorData.message
      lastMsg.isLoading = false
    }
  }
  
  const connect = async () => {
    await wsConnection.connect({
      onSessionId: handleSessionId,
      onMessage: handleMessage,
      onError: handleError,
    })
  }
  
  //
  // onMounted(() => {
  //   handleSessionId('24234')
  //
  //   const userMessage = MessageEntity.createUserMessage('Роскажи про перевірку диплома')
  //   messages.value.push(userMessage)
  //   const loadingMessage = MessageEntity.createLoadingMessage()
  //   messages.value.push(loadingMessage)
  //   handleMessage(mockData)
  // })
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
    currentSources.value = []
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
    currentSources,
    lastMessage,
    isLoading,
    hasMessages,
    connect,
    sendMessage,
    reset,
    disconnect,
  }
})
