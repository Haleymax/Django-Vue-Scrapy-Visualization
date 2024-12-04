<template>
    <span class="el-dropdown-link">
        个人信息<el-icon class="el-icon--right"> </el-icon>
    </span>
</template>

<script setup lang="ts" name="Avatar">
import { reactive, toRefs } from 'vue'
const state = reactive({
    circleUrl:
        'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
    squareUrl:
        'https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png',
    sizeList: ['small', '', 'large'] as const,
})

const { circleUrl, squareUrl, sizeList } = toRefs(state)
</script>

<style>
.el-dropdown-link {
    color: white;
}
</style>