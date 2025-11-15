<template>
  <ScrollPanel ref="scrollPanel" class="" style="height: 100%;">
    <div class="p-6 h-full">
      <div v-if="chatStore.messages.length === 0" class="flex flex-col items-center justify-center h-full">
        <div class="w-16 h-16 bg-gray-900 rounded-2xl flex items-center justify-center mb-4">
          <span class="text-4xl">👀</span>
        </div>
        <h1 class="text-3xl font-bold text-gray-900 mb-2 text-center">
          Вітаємо у вашому RAG-помічнику! 🤖
        </h1>
        <p class="text-gray-600 text-center max-w-2xl mb-4">
          Тут ви можете спілкуватися з системою для пошуку інформації та тестування запитів.
        </p>
        <p class="text-gray-500">
          Спробуйте поставити питання, щоб почати! 💬
        </p>
      </div>

      <div v-else class="pb-8">
        <MessageItem
          v-for="message in chatStore.messages"
          :key="message.id"
          :message="message"
        />
      </div>

    </div>
  </ScrollPanel>
</template>

<script setup>
import { ref, watch, nextTick } from 'vue';
import ScrollPanel from 'primevue/scrollpanel';
import MessageItem from './MessageItem.vue';
import { useChatStore } from '../../stores/useChatStore.js';

const chatStore = useChatStore();

const scrollPanel = ref(null);

const scrollToBottom = () => {
  nextTick(() => {
    if (scrollPanel.value) {
      const container = scrollPanel.value.$el.querySelector('.p-scrollpanel-content');
      if (container) {
        container.scrollTop = container.scrollHeight;
      }
    }
  });
};

watch(() => chatStore.messages.length, () => {
  scrollToBottom();
});
</script>
