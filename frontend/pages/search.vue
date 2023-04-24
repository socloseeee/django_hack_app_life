<script setup>
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css';
import axios from 'axios';
import { toast } from 'vue3-toastify';

const searchInput = ref('');
const dateInput = ref([]);
const isLoading = ref(false);

const radioOptopns = [
  {
    id: 1,
    value: 'nomer_zajavki',
    label: 'Поиск по заявке',
  },
  {
    id: 2,
    value: 'inn',
    label: 'Поиск по ИНН',
  },
  {
    id: 3,
    value: 'nomer_zajavki inn',
    label: 'Поиск по заявке и ИНН',
  },
];

const lifecycle = ref([]);

const radioInput = ref(radioOptopns[0]);

const formatDate = (date) => date.split('T')[0].split('-').reverse().join('.');

const find = async () => {
  if (isLoading.value) return;
  isLoading.value = true;

  try {
    const { data } = await axios.get(
      `${import.meta.env.VITE_API_URL}`,
      {
        params: {
          [radioInput.value.value]: searchInput.value,
          start_date: formatDate(dateInput?.value[0].toISOString()) || '',
          end_date: formatDate(dateInput?.value[1].toISOString()) || '',
        },
      },
      {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }
    );

    if (!data.length) {
      toast.info('Не найдено!');
      lifecycle.value = [];
      return;
    }
    lifecycle.value = data;
  } catch (error) {
    toast.error('Произошла ошибка на сервере...');
  }
  isLoading.value = false;
};
</script>

<template>
  <section class="w-full py-8 flex flex-col gap-8">
    <BaseRadio v-model="radioInput" :options="radioOptopns" />

    <VueDatePicker v-model="dateInput" range :enableTimePicker="false" />
    
    <BaseInput v-model="searchInput" @keyup.enter="find">
      <template #label> Поиск: </template>
    </BaseInput>
    <BaseButton :loading="isLoading" class="max-w-sm" @click="find">
      Найти
    </BaseButton>

    <div class="flex flex-col gap-1" v-if="lifecycle.length">
      <BaseLifecycle v-for="item in lifecycle" :key="item.date" :data="item" />
    </div>
  </section>
</template>
