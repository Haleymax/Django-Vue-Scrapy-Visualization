<template>
    <el-menu default-active="/home" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
        <template v-for="(item1, index1) in menuData">
            <el-sub-menu v-if="item1.children && item1.children.length > 0" :index="item1.id.toString()">
                <template #title>
                    <el-icon>
                        <Location />
                    </el-icon>
                    <span>{{ item1.name }}</span>
                </template>
                <template v-for="(item2, index2) in item1.children">
                    <el-menu-item class="el" :index="item2.path || item2.id.toString()">
                        {{ item2.name }}
                    </el-menu-item>
                </template>
            </el-sub-menu>

            <el-menu-item v-else :index="item1.id.toString()">
                <el-icon>
                    <IconMenu />
                </el-icon>
                <span>{{ item1.name }}</span>
            </el-menu-item>
        </template>
    </el-menu>
</template>

<script setup lang="ts" name='Menu'>
import { Location, Menu as IconMenu } from '@element-plus/icons-vue';
import { menuDataStore } from '@/store/menu'

const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath);
};

const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath);
};

const menuData = menuDataStore().menuDate

</script>

<style>
.el {
    background-color: #b2b6b6;
}
</style>