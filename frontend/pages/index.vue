<script lang="ts" setup>
import axios from 'axios';
import { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const state = reactive({ isLoading: false, hasFiles: false });
let files: File[];

const fileUpload = async (value: any) => {
  files = value;
  state.hasFiles = !!files?.length;
};

const uploadOnServer = async () => {
  if (state.isLoading || !state.hasFiles) return;

  state.isLoading = true;
  let formData = new FormData();

  files.forEach((file) => {
    formData.append('files', file);
  });

  let code;
  try {
    const data = await axios.post(
      `${import.meta.env.VITE_API_URL}/files-upload`,
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }
    );

    code = data.status;
  } catch (error: any) {
    code = error?.request?.status || 500;
  }

  switch (code) {
    case 500:
      toast.error('Произошла внутренняя ошибка...', {
        autoClose: 3000,
      });
      break;
    case 404:
      toast.error('404 Произошла внутренняя ошибка...', {
        autoClose: 3000,
      });
      break;
    case 415:
      toast.error('Неверный тип файла!', {
        autoClose: 3000,
      });
      break;
    default:
      toast.success('Файл успешно загружен на сервер', {
        autoClose: 3000,
      });
      break;
  }

  state.isLoading = false;
};
</script>

<template>
  <section class="py-8 flex flex-col gap-4">
    <h1 class="text-2xl">Главная страница</h1>
    <p>Здесь вы можете загрузить файлы для дальнейшей работы</p>
    <div class="flex flex-col items-center gap-4 justify-center">
      <BaseFileInput @fileUpload="fileUpload">
        <template #description>
          <div class="mb-2 text-sm text-gray-500">
            Перенесите файлы с данными в эту область или
            <span class="font-bold">нажмите</span> чтобы загрузить
          </div>
          <div class="mb-2 text-xs text-gray-500">
            Файлы должен быть в формате .xlsx
          </div>
        </template>
      </BaseFileInput>
      <BaseButton
        class="max-w-sm"
        :loading="state.isLoading"
        :disabled="!state.hasFiles"
        @click="uploadOnServer"
        >Отправить на сервер</BaseButton
      >
    </div>
  </section>
</template>
