<script setup>
import { defineProps, defineEmits, computed } from 'vue';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';

const props = defineProps({
  visible: {
    type: Boolean,
    required: true
  },
  source: {
    type: Object,
    default: null
  }
});

const emit = defineEmits(['update:visible']);

const closeModal = () => {
  emit('update:visible', false);
};

const handleDownload = () => {
  console.log('Завантаження документа:', props.source?.metadata?.fileName);
};
</script>

<template>
  <Dialog
    :visible="visible"
    @update:visible="closeModal"
    :modal="true"
    :closable="true"
    :draggable="false"
    class="w-full max-w-3xl"
    header="Деталі джерела"
  >
    <div v-if="source" class="space-y-4">
      <div class="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <div class="flex items-center justify-between mb-2">
          <h3 class="text-lg font-semibold text-gray-900">
            Джерело #{{ source.index }}
          </h3>
          <span class="px-3 py-1 bg-green-100 text-green-800 text-sm font-medium rounded-full">
            {{ source.formattedScore }}
          </span>
        </div>
        <p class="text-sm text-gray-600">Оцінка релевантності</p>
      </div>

      <div class="space-y-3">
        <h4 class="text-sm font-semibold text-gray-700 uppercase tracking-wide">Метадані файлу</h4>
        <div class="grid grid-cols-2 gap-3 bg-gray-50 rounded-lg p-4">
          <div>
            <p class="text-xs text-gray-500 mb-1">Назва файлу</p>
            <p class="text-sm font-medium text-gray-900">{{ source.metadata.fileName }}</p>
          </div>
          <div>
            <p class="text-xs text-gray-500 mb-1">Тип файлу</p>
            <p class="text-sm font-medium text-gray-900">{{ source.metadata.fileType }}</p>
          </div>
          <div>
            <p class="text-xs text-gray-500 mb-1">Розмір</p>
            <p class="text-sm font-medium text-gray-900">{{ source.formattedFileSize }}</p>
          </div>
          <div>
            <p class="text-xs text-gray-500 mb-1">Сторінка</p>
            <p class="text-sm font-medium text-gray-900">{{ source.metadata.pageLabel || 'N/A' }}</p>
          </div>
          <div class="col-span-2">
            <p class="text-xs text-gray-500 mb-1">Остання зміна</p>
            <p class="text-sm font-medium text-gray-900">{{ source.metadata.lastModifiedDate }}</p>
          </div>
        </div>
      </div>

      <div class="space-y-2">
        <h4 class="text-sm font-semibold text-gray-700 uppercase tracking-wide">Текст джерела</h4>
        <div class="bg-gray-50 rounded-lg p-4 max-h-96 overflow-y-auto">
          <p class="text-sm text-gray-800 whitespace-pre-wrap leading-relaxed">{{ source.text }}</p>
        </div>
      </div>

      <div class="flex justify-end pt-4 border-t border-gray-200">
        <Button
          label="Завантажити документ (заглушка)"
          icon="pi pi-download"
          @click="handleDownload"
          class="p-button-outlined"
          disabled
        />
      </div>
    </div>
  </Dialog>
</template>
