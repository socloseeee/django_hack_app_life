<script setup>
defineProps(['data']);

const getStatus = (status) => {
  switch (true) {
    case status.includes('Закрыт'):
      return 'bg-green-300';
    case status.includes('Удалена') || status.includes('Тест'):
      return 'bg-red-300';
    default:
      return 'bg-yellow-300';
  }
};
</script>

<template>
  <div
    class="shadow-md flex gap-2 px-2 py-4 bg-rtk-grey text-rtk-black rounded-lg"
  >
    <div class="date">Дата: {{ data.date }}</div>
    <div class="date">Номер заявки: {{ data['nomer_zajavki'] }}</div>
    <div class="date">Клиент: {{ data['klient_field'] }}</div>
    <div class="date">ИНН: {{ data['inn'] }}</div>
    <div :class="getStatus(data['status'])">Статус: {{ data['status'] }}</div>
  </div>
</template>
