<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  sources: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['source-click']);

const handleSourceClick = (source) => {
  emit('source-click', source);
};
</script>

<template>
  <div v-if="sources && sources.length > 0" class="mt-4 pt-3 border-t border-gray-200">
    <div class="flex items-center gap-2">
      <span class="text-sm font-medium text-gray-700">Sources:</span>
      <div class="flex gap-2">
        <button
          v-for="source in sources"
          :key="source.id"
          @click="handleSourceClick(source)"
          class="w-8 h-8 flex items-center justify-center text-sm font-medium text-blue-600 hover:text-blue-800 hover:bg-blue-50 border border-blue-300 rounded transition-colors duration-150"
        >
          {{ source.index }}
        </button>
      </div>
    </div>
  </div>
</template>
