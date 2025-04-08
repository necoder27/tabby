<template>
  <div id="system-info-container">
    <div class="system-info-item">
      <p class="system-info-label">os</p>
      <p>{{ macosVersion }}</p>
    </div>
    <div class="system-info-item">
      <p class="system-info-label">uptime</p>
      <p>{{ uptime }}</p>
    </div>
    <div class="system-info-item">
      <p class="system-info-label">ram</p>
      <p>{{ memoryUsage }}</p>
    </div>
    <div class="system-info-item">
      <p class="system-info-label">disk</p>
      <p>{{ diskUsage }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
  import {ref,onMounted} from "vue";
  import apiClient from '@/api';

  const macosVersion = ref<string>("");
  const uptime = ref<string>("");
  const memoryUsage = ref<string>("");
  const diskUsage = ref<string>("");

  async function getMacOSVersion() {
    const response = await apiClient.get("/system/os");
    macosVersion.value = response.data;
  }

  async function getUptime() {
    const response = await apiClient.get("/system/uptime");
    uptime.value = response.data;
  }

  async function getMemoryUsage() {
    const response = await apiClient.get("/system/memory");
    memoryUsage.value = response.data;
  }

  async function getDiskUsage() {
    const response = await apiClient.get("/system/disk");
    diskUsage.value = response.data;
  }

  onMounted(async () => {
    await getMacOSVersion();
    await getUptime();
    await getMemoryUsage();
    await getDiskUsage();
  })
</script>

<style scoped>
  #system-info-container {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    font-weight: 100;
    font-size: 2vh;
  }

  .system-info-item {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin: 0;
    height: fit-content;

    p {
      margin: 0;
    }
  }

  .system-info-label {
    font-weight: 300;
  }
</style>
