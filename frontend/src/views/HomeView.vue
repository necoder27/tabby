<template>
  <div id="home-view-container">
    <div id="home-view-row-0">
      <WeatherComponent />
      <MainComponent />
    </div>
    <ClockComponent />
  </div>
</template>

<script setup lang="ts">
  import WeatherComponent from '@/components/WeatherComponent.vue';
  import MainComponent from '@/components/MainComponent.vue';
  import ClockComponent from '@/components/ClockComponent.vue';
</script>

<style scoped>
  #home-view-container {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
  }

  #home-view-row-0 {
    display: flex;
    flex-direction: row;
    height: 60%;
    width: 100%;
    justify-content: space-between;
  }
</style>
