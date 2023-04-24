<script setup>
const props = defineProps({
  menuItems: {
    type: Array,
    required: true,
  },
});
</script>

<template>
  <nav class="flex flex-col gap-2 px-8 py-4">
    <NuxtLink
      v-for="item in menuItems"
      :key="item.label"
      :to="item.link"
      class="item flex px-4 py-2 hover:bg-rtk-orange hover:bg-opacity-20 rounded-md transition-all"
      activeClass="text-rtk-orange"
    >
      {{ item.label }}
    </NuxtLink>
  </nav>
</template>
