<template>
  <div class="h-full flex flex-col">
    <div v-if="documentsStore.error" class="p-4">
      <div class="bg-red-50 border border-red-200 text-red-800 px-4 py-3 rounded">
        <div class="flex items-center gap-2">
          <i class="pi pi-exclamation-triangle"></i>
          <span class="font-medium">Помилка завантаження документів</span>
        </div>
        <p class="text-sm mt-1">{{ error }}</p>
      </div>
    </div>

    <div v-else class="flex-1 overflow-auto">
      <DataTable
        :value="documentsStore.isLoading ? new Array(4) : documentsStore.documents"
        class="text-md"
      >
        <template #empty v-if="documentsStore.isLoading">
          <div class="text-center text-gray-500 py-8">
            <i class="pi pi-inbox text-5xl mb-4 block"></i>
            <p class="text-lg font-medium">Немає документів</p>
            <p class="text-sm mt-1">Документи з'являться тут після завантаження</p>
          </div>
        </template>

        <Column header="" class="w-[24px] !pr-0">
          <template #body="{ data }">
            <div class="flex items-center justify-center w-[24px] h-[24px]">
              <Skeleton width="1.5rem" height="1.5rem" v-if="documentsStore.isLoading" />
              <i :class="getFileIcon(data.fileType)"  v-else class="text-2xl text-gray-600"></i>
            </div>
          </template>
        </Column>

        <Column field="name" header="File Name" class="min-w-[300px]">
          <template #body="{ data }">
            <Skeleton width="80%" height="1.5rem" v-if="documentsStore.isLoading"/>
            <div class="font-medium text-gray-900 truncate" :title="data.name" v-else>
              {{ data.name }}
            </div>
          </template>
        </Column>

        <Column field="status" header="Status" class="w-32">
          <template #body="{ data }">
            <Skeleton width="5rem" height="1.5rem" borderRadius="16px" v-if="documentsStore.isLoading"/>
            <Badge
                v-else
                :value="getStatusLabel(data.status)"
                :severity="getStatusSeverity(data.status)"
            />
          </template>
        </Column>

        <Column field="fileSize" header="File Size" class="w-32">
          <template #body="{ data }">
            <Skeleton width="4rem" height="1.5rem" v-if="documentsStore.isLoading"/>
            <span class="text-gray-700" v-else>{{ data.fileSize }}</span>
          </template>
        </Column>

        <Column field="fileType" header="File Type" class="w-32">
          <template #body="{ data }">
            <Skeleton width="3rem" height="1.5rem" v-if="documentsStore.isLoading"/>
            <span class="text-gray-600 uppercase font-mono text-xs" v-else>
              {{ data.fileType || 'N/A' }}
            </span>
          </template>
        </Column>
      </DataTable>
    </div>
  </div>
</template>

<script setup>

import {onMounted} from "vue";
import {useDocumentsStore} from "../../stores/useDocumentsStore.js";
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import Badge from 'primevue/badge';
import Skeleton from 'primevue/skeleton';

const documentsStore = useDocumentsStore();

const getFileIcon = (fileType) => {
  const type = fileType?.toLowerCase();
  const iconMap = {
    'pdf': 'pi pi-file-pdf',
    'doc': 'pi pi-file-word',
    'docx': 'pi pi-file-word',
    'xls': 'pi pi-file-excel',
    'xlsx': 'pi pi-file-excel',
    'txt': 'pi pi-file',
    'md': 'pi pi-file-edit',
  };
  return iconMap[type] || 'pi pi-file';
};

const getStatusLabel = (status) => {
  const statusMap = {
    'success': 'Загружено',
    'completed': 'Завершено',
    'processing': 'Обробка',
    'error': 'Помилка',
    'pending': 'Очікує',
  };
  return statusMap[status?.toLowerCase()] || status;
};

const getStatusSeverity = (status) => {
  const statusLower = status?.toLowerCase();
  if (statusLower === 'success' || statusLower === 'completed') return 'success';
  if (statusLower === 'error') return 'danger';
  if (statusLower === 'processing') return 'info';
  if (statusLower === 'pending') return 'warning';
  return 'secondary';
};

onMounted(() => {
  documentsStore.fetchDocuments();
});
</script>
