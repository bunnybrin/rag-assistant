<template>
  <div class="card flex justify-center">
    <SelectButton v-model="mode" :options="options" optionLabel="name" option-value="value"/>
  </div>
</template>

<script setup>
import {ref} from 'vue';
import {SelectButton} from "primevue";

const mode = defineModel('modelValue', {default: 'chatbot'});

const options = ref([
  {name: 'Чатбот', value: 'chatbot',},
  {name: 'Джерела', value: 'sources',}
]);
</script>