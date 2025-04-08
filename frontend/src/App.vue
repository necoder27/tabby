<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div id="main-container">
    <video autoplay loop muted>
      <source src="@/assets/imgs/cat-sakura-street-pixel-moewalls-com.mp4" type="video/mp4">
    </video>
    <RouterView />
  </div>
</template>

<style scoped>
  #main-container {
    height: 100vh;
    width: 100vw;
  }

  video {
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
