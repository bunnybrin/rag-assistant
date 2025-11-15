<template>
  <div class="flex flex-col h-screen bg-white">
    <header class="border-b border-gray-100 bg-white px-6 py-4">
      <div class="flex items-center justify-between flex-col md:flex-row">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-gray-900 rounded-lg flex items-center justify-center">
            <span class="text-2xl">👀</span>
          </div>
          <h1 class="text-xl font-bold text-gray-900">RAG Playground</h1>
        </div>

        <div class="flex items-center gap-4">
          <ChatMode :model-value="currentMode" @update:model-value="setActiveTab"/>
        </div>
      </div>
    </header>

    <div class="flex flex-1 bg-gray-50 px-12 py-8">
      <div class="flex-1 flex flex-col min-w-0 max-w-4xl mx-auto w-full h-full max-h-[500px]">
        <div v-if="currentMode === 'chatbot'" class="flex flex-col flex-1 h-full">
          <MessageList/>
          <ChatInput/>
        </div>
        <SourcesView v-else-if="currentMode === 'sources'"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import ChatMode from './ChatMode.vue';
import MessageList from "./MessageList.vue";
import ChatInput from "./ChatInput.vue";
import SourcesView from "./SourcesView.vue";
import {useUrlTabs} from "../../utils/useUrlTabs.js";

const { activeTab: currentMode, setActiveTab } = useUrlTabs({
  tabs: ['chatbot', 'sources'],
  defaultTab: 'chatbot',
  paramName: 'mode'
});
</script>
