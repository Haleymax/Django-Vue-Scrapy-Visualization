<script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'
import Layout from '@/layouts/AppLayout.vue'
import Home from './views/Home.vue';
</script>

<template>
  <!-- <Layout></Layout> -->
    <router-link to="/home">home</router-link>
  <RouterView/>
</template>

<style scoped></style>
