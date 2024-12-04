<template>
    <el-dropdown>
        <div v-if="isLoggedIn">
            <el-dropdown-menu>
                <el-dropdown-item command="a">个人信息</el-dropdown-item>
                <el-dropdown-item command="b">设置</el-dropdown-item>
                <el-dropdown-item command="c">关于</el-dropdown-item>
                <el-dropdown-item command="d" disabled>Action 4</el-dropdown-item>
                <el-dropdown-item command="e" divided>退出登陆</el-dropdown-item>
            </el-dropdown-menu>
        </div>
        <div v-else>
            <el-dropdown-menu>
                <el-dropdown-item @click="showLoginForm.set_true()">注册/登录</el-dropdown-item>
            </el-dropdown-menu>
        </div>
    </el-dropdown>
</template>

<script setup lang="ts" name="DropdownMenu">
import { ref } from 'vue';
import {useLoginForm} from '@/store/home'

const isLoggedIn = ref(false);
const showLoginForm = useLoginForm();
</script>

<style>

</style>
