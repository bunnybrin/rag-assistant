<template>
  <div :class="['flex gap-3 mb-4', message.isUser ? 'justify-end' : 'justify-start']">
    <div v-if="!message.isUser" class="flex-shrink-0">
      <div class="w-10 h-10 bg-gray-900 rounded-lg flex items-center justify-center">
        <span class="text-2xl">🤖</span>
      </div>
    </div>

    <div :class="['max-w-3xl', message.isUser ? 'order-first' : '']">
      <div
        :class="[
          'rounded-lg px-4 py-3',
          message.isUser
            ? 'bg-blue-600 text-white ml-auto'
            : 'bg-white border border-gray-200 text-gray-900'
        ]"
      >
        <div v-if="message.isLoading" class="flex items-center gap-2">
          <div class="flex gap-1">
            <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 0ms"></span>
            <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 150ms"></span>
            <span class="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style="animation-delay: 300ms"></span>
          </div>
          <span class="text-sm text-gray-500">Думаю...</span>
        </div>

        <div v-else-if="message.error" class="text-red-600">
          <p class="font-medium">Помилка:</p>
          <p class="text-sm">{{ message.error }}</p>
        </div>

        <div v-else class="whitespace-pre-wrap break-words">
          {{ message.content }}
        </div>
      </div>

      <div v-if="!message.isUser && !message.isLoading" class="text-xs text-gray-400 mt-1 ml-1">
        {{ message.formattedTime }}
      </div>
    </div>

    <div v-if="message.isUser" class="flex-shrink-0">
      <div class="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
        </svg>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  message: {
    type: Object,
    required: true,
  },
});
</script>
