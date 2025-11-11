<template>
  <Toast />
  <ChatLayout />
</template>

<script setup>
import { onMounted, onUnmounted, watch } from 'vue';
import { useToast } from 'primevue/usetoast';
import Toast from 'primevue/toast';
import ChatLayout from './components/chat/ChatLayout.vue';
import { useChatStore } from './stores/chat';

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
  await chatStore.connect();
});

onUnmounted(() => {
  chatStore.disconnect();
});
</script>
