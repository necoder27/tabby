<template>
  <div id="clock-container">
    <p id="clock">{{ time }}</p>
  </div>
</template>

<script setup lang="ts">
  import {ref} from "vue";

  const time = ref();

  function setCurrentTime() {
    time.value = new Date().toLocaleTimeString();
  }

  setInterval(setCurrentTime, 1000)
</script>

<style scoped>
  #clock-container {
    bottom: 0;
    height: 40%;
    margin: 4vh 2vw;
    font-size: 10vh;
    font-weight: 600;
  }

  #clock {
    margin: 0;
    position: absolute;
    bottom: 0;
  }
</style>
