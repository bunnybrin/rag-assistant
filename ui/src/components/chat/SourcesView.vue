<template>
  <div class="h-full">
    <div :key="doc.id" v-for="doc in sdf" class="p-4 border-b border-gray-200 text-gray-900 whitespace-pre-wrap">
      {{ doc.text }}
    </div>
  </div>
</template>

<script setup>


import {ref} from "vue";
import {DocumentsRepository} from "../../repositories/DocumentsRepository.js";

const sdf = ref([])

DocumentsRepository.getDocuments().then(documents => {
  sdf.value = documents.documents
})

</script>


<style scoped>

</style>