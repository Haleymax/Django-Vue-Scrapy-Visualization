<script setup lang="ts" name="app">
import Home from './views/Home.vue'
import router from './router';

const goToHome= () => {
  router.push('/home');
};


</script>

<template>
  <router-view></router-view>
</template>

<style scoped></style>