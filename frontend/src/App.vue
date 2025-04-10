<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import BackgroundImage from "@/assets/imgs/cherry-blossoms-1317308.jpg";
</script>

<template>
  <div id="main-container">
    <img :src="BackgroundImage" alt="">
    <RouterView />
  </div>
</template>

<style scoped>
  #main-container {
    height: 100vh;
    width: 100vw;
  }

  img {
    position: fixed;
    top: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
  }

  RouterView {
    z-index: 99;
  }
</style>
