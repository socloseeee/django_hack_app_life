<script setup>
const props = defineProps({
  tag: {
    type: String,
    default: 'button',
  },
  disabled: {
    type: Boolean,
    default: false,
  },
  loading: {
    type: Boolean,
    default: false,
  },
  variant: {
    type: String,
    default: 'primary',
  },
  to: {
    type: String,
  },
});

const { tag, disabled, loading, to, variant } = toRefs(props);

const btnClass = computed(() => {
  return {
    'cursor-not-allowed opacity-70':
      disabled.value === true || loading.value === true,
    'button base-button rounded-lg px-6 py-3 inline-flex align-middle align-items-center justify-center font-medium focus:outline-none border-2': true,
  };
});

const colorVariants = computed(() => {
  switch (variant.value) {
    case 'primary':
      return 'border-transparent bg-rtk-orange hover:shadow-md text-white';
    case 'danger':
      return 'border-red-600 bg-red-600 hover:bg-red-700 hover:border-red-700 text-white';
    default:
      break;
  }
});
</script>

<template>
  <component
    :is="tag"
    :disabled="disabled"
    :class="[btnClass, colorVariants]"
    :variant="variant"
    :href="to"
  >
    <template v-if="!loading">
      <slot />
    </template>
    <BaseSpinner v-else />
  </component>
</template>
