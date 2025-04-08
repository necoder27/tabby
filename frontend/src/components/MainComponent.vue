<template>
  <div id="main-component-container">
    <GreetingComponent />
    <SystemInformationComponent />
  </div>
</template>

<script setup lang="ts">
  import GreetingComponent from './GreetingComponent.vue';
  import SystemInformationComponent from './SystemInformationComponent.vue';
</script>

<style scoped>
  #main-component-container {
    background-color: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(5px);
    border-radius: 25px;
    display: flex;
    flex-direction: column;
    padding: 2vh 2vw;
    margin: 4vh 2vw;
    width: fit-content;
    height: fit-content;
    font-size: 2vh;
  }
</style>
