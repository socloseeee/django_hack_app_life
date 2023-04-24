<script setup>
defineProps({ modelValue: { type: Object }, options: { type: Array } });
defineEmits(['update:modelValue']);
</script>

<template>
  <div class="radio flex items-center gap-2">
    <div
      v-for="option in options"
      :key="option.id"
      class="flex items-center gap-2 p-4 border cursor-pointer hover:bg-white bg-rtk-grey border-gray-200 rounded"
      @click="$emit('update:modelValue', option)"
    >
      <input
        type="radio"
        :value="option.value"
        :checked="modelValue.value === option.value"
        :name="option.value"
        class="w-4 h-4 cursor-pointer text-rtk-orange bg-gray-100 border-gray-300 focus:ring-blue-500"
        @input="$emit('update:modelValue', option)"
      />
      <label
        :for="option.value"
        class="ml-2 text-sm cursor-pointer font-medium text-rtk-black"
        >{{ option.label }}</label
      >
    </div>
  </div>
</template>
