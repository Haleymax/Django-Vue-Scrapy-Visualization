<template>
    <div class="box">
        <!-- <SignIn></SignIn> -->
         <sign_up></sign_up>
    </div>
</template>

<script setup lang="ts" name="Login">
import SignIn from '@/views/login/sign_in.vue'
import sign_up from '@/views/login/sign_up.vue'
</script>

<style scoped>
.box {
    width: 100%;
    height: 100%;
    background-color: white;

    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
</style>