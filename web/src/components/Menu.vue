<template>
    <el-menu default-active="/home"  class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
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

const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath);
};

const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath);
};

let menuData = [
    {
        id: 1,
        name: 'Menu 1',
        children: [
            { id: 11, name: 'Menu 1-1', path: '/menu1-1' },
            { id: 12, name: 'Menu 1-2', path: '/menu1-2' },
            { id: 13, name: 'Menu 1-3', path: '/menu1-3' },
        ],
    },
    {
        id: 2,
        name: 'Menu 2',
        children: [
            { id: 21, name: 'Menu 2-1', path: '/menu2-1' },
            { id: 22, name: 'Menu 2-2', path: '/menu2-2' },
            { id: 23, name: 'Menu 2-3', path: '/menu2-3' },
        ],
    },
    {
        id: 3,
        name: 'Menu 3',
        children: [
            { id: 31, name: 'Menu 3-1', path: '/menu3-1' },
            { id: 32, name: 'Menu 3-2', path: '/menu3-2' },
            { id: 33, name: 'Menu 3-3', path: '/menu3-3' },
        ],
    },
    {
        id: 4,
        name: 'Menu 4',
        path: '/menu4'
    },
];
</script>

<style>
.el {
    background-color: #b2b6b6;
}
</style>