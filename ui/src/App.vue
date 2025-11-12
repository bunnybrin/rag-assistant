<template>
  <Toast />
  <ChatLayout />
</template>

<script setup>
import { onMounted, onUnmounted, watch } from 'vue';
import { useToast } from 'primevue/usetoast';
import Toast from 'primevue/toast';
import ChatLayout from './components/chat/ChatLayout.vue';
import { useChatStore } from './stores/useChatStore.js';
import {useDocumentsStore} from "./stores/useDocumentsStore.js";

const documentsStore = useDocumentsStore();
const chatStore = useChatStore();
const toast = useToast();

watch(() => chatStore.error, (newError) => {
  if (newError) {
    toast.add({
      severity: 'error',
      summary: 'Помилка',
      detail: newError,
      life: 5000
    });
  }
});

onMounted(async () => {
  chatStore.connect();
  documentsStore.fetchDocuments();
});

onUnmounted(() => {
  chatStore.disconnect();
});
</script>
