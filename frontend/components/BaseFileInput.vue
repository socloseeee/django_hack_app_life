<template>
  <div
    class="max-w-2xl text-center bg-gray-100 border rounded-md border-gray-300"
    @dragover="dragover"
    @dragleave="dragleave"
    @drop="drop"
  >
    <input
      id="assetsFieldHandle"
      ref="file"
      type="file"
      class="opacity-0 overflow-hidden absolute"
      accept=".xlsx"
      multiple
      @change="onChange"
    />

    <label
      for="assetsFieldHandle"
      class="p-10 flex flex-col items-center cursor-pointer"
    >
      <svg
        aria-hidden="true"
        class="mb-3 w-10 h-10 text-gray-400"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
        />
      </svg>
      <slot name="description" />
    </label>

    <div
      v-if="fileList.length"
      class="items flex flex-wrap gap-4 border-t-[1px] py-4 border-t-rtk-black"
    >
      <div
        v-for="file in fileList"
        v-cloak
        class="p-2 text-center bg-gray-100 rounded-md text-md text-gray-500 flex gap-5 justify-center"
      >
        <i class="fa fa-file" />
        {{ file.name }}
        <button
          class="text-red-500"
          type="button"
          title="Удалить"
          @click="remove(fileList.indexOf(file))"
        >
          Удалить
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  emits: { fileUpload: null },
  data() {
    return {
      fileList: [],
    };
  },
  methods: {
    onChange() {
      this.fileList = [...this.fileList, ...this.$refs.file.files];
      this.$emit('fileUpload', this.fileList);
    },
    remove(i) {
      this.fileList.splice(i, 1);
    },
    dragover(event) {
      event.preventDefault();

      if (!event.currentTarget.classList.contains('bg-blue-200')) {
        event.currentTarget.classList.remove('bg-gray-100');
        event.currentTarget.classList.add('bg-blue-200');
      }
    },
    dragleave(event) {
      event.currentTarget.classList.add('bg-gray-100');
      event.currentTarget.classList.remove('bg-blue-200');
    },
    drop(event) {
      event.preventDefault();
      if (event.dataTransfer.files.length) {
        this.fileList = [...this.fileList, ...event.dataTransfer.files];
        this.$emit('fileUpload', this.fileList);
      }

      event.currentTarget.classList.add('bg-gray-100');
      event.currentTarget.classList.remove('bg-blue-200');
    },
  },
};
</script>
