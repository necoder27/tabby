<template>
  <div id="greeting-container">
    <p id="greeting">{{ greeting }}</p>
  </div>
</template>

<script setup lang="ts">
  import {ref,onMounted} from "vue";
  import apiClient from '@/api';

  const greeting = ref<string>("");

  async function getGreeting() {
    const response = await apiClient.get("/greeting");
    greeting.value = response.data
  }

  onMounted(async () => {
    await getGreeting();
  })
</script>

<style scoped>
  #greeting-container {
    display: flex;
    flex-direction: column;
    text-align: center;
    width: 100%;
    margin-bottom: 2vh;
  }

  #greeting {
    margin: 0;
    font-size: 4vh;
    font-weight: 600;
  }
</style>
