<template>
  <div class="flex flex-col h-screen bg-white">
    <header class="border-b border-gray-100 bg-white px-6 py-4">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-gray-900 rounded-lg flex items-center justify-center">
            <span class="text-2xl">👀</span>
          </div>
          <h1 class="text-xl font-bold text-gray-900">RAG Assistant Playground</h1>
        </div>

        <div class="flex items-center gap-4">
          <ChatMode v-model="currentMode"/>
        </div>
      </div>
    </header>

    <div class="flex flex-1 bg-gray-50 px-12 py-8">
      <div class="flex-1 flex flex-col min-w-0 max-w-4xl mx-auto w-full h-full max-h-[calc(100vh-75px)]">
        <template v-if="currentMode === 'chatbot'" >
          <MessageList/>
          <ChatInput/>
        </template>
        <SourcesView v-else-if="currentMode === 'sources'"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref} from 'vue';
import ChatMode from './ChatMode.vue';
import MessageList from "./MessageList.vue";
import ChatInput from "./ChatInput.vue";
import SourcesView from "./SourcesView.vue";

const currentMode = ref('chatbot');
</script>
