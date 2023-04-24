<script setup>
defineProps(['modelValue']);
defineEmits(['update:modelValue']);
</script>

<template>
  <div>
    <label
      for="default-input"
      class="block mb-2 text-md font-medium dark:text-white"
      ><slot name="label"> </slot
    ></label>
    <input
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      type="text"
      id="default-input"
      class="bg-rtk-gray text-rtk-black focus-visible:border-none border-none text-sm rounded-lg focus:ring-rtk-orange focus:border-rtk-orange block w-full p-2.5"
    />
  </div>
</template>
