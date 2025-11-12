import {defineStore} from 'pinia'
import {ref} from 'vue'
import {DocumentsRepository} from '../repositories/DocumentsRepository'

export const useDocumentsStore = defineStore('documents', () => {
  const documents = ref([])
  const isLoading = ref(false)
  const error = ref(null)

  const fetchDocuments = async () => {
    isLoading.value = true
    error.value = null

    try {
      const response = await DocumentsRepository.getDocuments()
      documents.value = response.documents || []
    } catch (err) {
      console.error('Error loading documents:', err)
      error.value = err.message || 'Не вдалося завантажити документи'
    } finally {
      isLoading.value = false
    }
  }

  const reset = () => {
    documents.value = []
    error.value = null
  }

  return {
    documents,
    isLoading,
    error,
    fetchDocuments,
    reset,
  }
})
