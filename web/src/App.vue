<script setup lang="ts" name="app">
import Home from './views/Home.vue'
import router from './router';
import Login from './views/login/Login.vue';
import Admin from './views/admin/Admin.vue';
import EchartsComponent from '@/views/chart/SalesData.vue'


</script>

<template>

  <router-view></router-view>
   <!-- <Login></Login> -->
    <!-- <Admin></Admin>
     <EchartsComponent></EchartsComponent> -->
</template>

<style scoped></style>