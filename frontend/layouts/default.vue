<script setup>
const menu_items = [
  {
    label: 'Главная',
    link: '/',
  },
  {
    label: 'Поиск',
    link: '/search',
  },
  {
    label: 'Заявки без активности',
    link: '/last-activity',
  },
];
</script>

<template>
  <div class="min-h-screen">
    <BaseHeader />
    <div class="min-h-[89vh] text-rtk-grey bg-rtk-dark-blue">
      <div class="flex gap-4">
        <div class="menu">
          <BaseMenu :menu-items="menu_items" />
        </div>
        <div class="content w-full px-4">
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>
