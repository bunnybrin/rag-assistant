<template>
  <div class="p-4 bg-white border-t border-gray-200">
    <div class="flex gap-3 items-end max-w-4xl mx-auto">
      <Textarea
        v-model="inputMessage"
        placeholder="Type a message"
        :autoResize="true"
        rows="1"
        :maxRows="6"
        class="flex-1"
        :disabled="!chatStore.isConnected || chatStore.isLoading"
        @keydown.enter.exact.prevent="handleSend"
      />
      <Button
        label="Send message"
        icon="pi pi-send"
        :disabled="!canSend"
        :loading="chatStore.isLoading"
        @click="handleSend"
        icon-pos="right"
        severity="contrast"
        class="flex-shrink-0"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';
import { useChatStore } from '../../stores/chat';

const chatStore = useChatStore();

const inputMessage = ref('');

const canSend = computed(() => {
  return chatStore.isConnected && !chatStore.isLoading && inputMessage.value.trim().length > 0;
});

const handleSend = () => {
  if (!canSend.value) return;

  const message = inputMessage.value.trim();
  if (message) {
    chatStore.sendMessage(message);
    inputMessage.value = '';
  }
};
</script>
