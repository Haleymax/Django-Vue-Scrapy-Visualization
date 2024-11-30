<template>
    <el-container>
        <el-header>
            <el-row>
                <el-col :span="4" class="col1">
                    爬虫数据可视化管理平台
                </el-col>
                <el-col :span="1">
                    关于
                </el-col>
                <el-col :span="2">
                    设置
                </el-col>
                <el-col :span="3">
                    个人信息
                </el-col>
                <el-col :span="4">
                    退出
                </el-col>
                <el-col :span="5">
                    <el-dropdown>
                        <span class="el-dropdown-link">
                            Dropdown List
                            <el-icon class="el-icon--right">
                                <arrow-down />
                            </el-icon>
                        </span>
                        <template #dropdown>
                            <el-dropdown-menu>
                                <el-dropdown-item>设置</el-dropdown-item>
                                <el-dropdown-item>修改</el-dropdown-item>
                                <el-dropdown-item>个人资料</el-dropdown-item>
                                <el-dropdown-item disabled>关于</el-dropdown-item>
                                <el-dropdown-item divided>退出</el-dropdown-item>
                            </el-dropdown-menu>
                        </template>
                    </el-dropdown>
                </el-col>
            </el-row>
        </el-header>
        <el-container>
            <el-aside width="200px">
                <el-row class="tac">
                    <el-col :span="12">
                        <h5 class="mb-2">Custom colors</h5>
                        <el-menu active-text-color="#ffd04b" background-color="#545c64" class="el-menu-vertical-demo"
                            default-active="2" text-color="#fff" @open="handleOpen" @close="handleClose">
                            <el-sub-menu index="1">
                                <template #title>
                                    <el-icon>
                                        <location />
                                    </el-icon>
                                    <span>Navigator One</span>
                                </template>
                                <el-menu-item-group title="Group One">
                                    <el-menu-item index="1-1">item one</el-menu-item>
                                    <el-menu-item index="1-2">item two</el-menu-item>
                                </el-menu-item-group>
                                <el-menu-item-group title="Group Two">
                                    <el-menu-item index="1-3">item three</el-menu-item>
                                </el-menu-item-group>
                                <el-sub-menu index="1-4">
                                    <template #title>item four</template>
                                    <el-menu-item index="1-4-1">item one</el-menu-item>
                                </el-sub-menu>
                            </el-sub-menu>
                            <el-menu-item index="2">
                                <el-icon><icon-menu /></el-icon>
                                <span>Navigator Two</span>
                            </el-menu-item>
                            <el-menu-item index="3" disabled>
                                <el-icon>
                                    <document />
                                </el-icon>
                                <span>Navigator Three</span>
                            </el-menu-item>
                            <el-menu-item index="4">
                                <el-icon>
                                    <setting />
                                </el-icon>
                                <span>Navigator Four</span>
                            </el-menu-item>
                        </el-menu>
                    </el-col>
                </el-row>
            </el-aside>

            <el-main>Main</el-main>
        </el-container>
    </el-container>
</template>

<script setup lang="ts" name='Layout'>
import { ArrowDown } from '@element-plus/icons-vue'
import {
    Document,
    Menu as IconMenu,
    Location,
    Setting,
} from '@element-plus/icons-vue'
const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
</script>

<style scoped>
.el-row {
    align-items: center;
    vertical-align: middle;
    padding-top: 10px;
}

.el-row:last-child {
    margin-bottom: 0;
    width: auto;
}

.el-col {
    border-radius: 4px;
    width: auto;
    background-color: rgb(63, 75, 4);
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}

.col1 {
    color: black;
}

.example-showcase .el-dropdown-link {
    cursor: pointer;
    color: var(--el-color-primary);
    display: flex;
    align-items: center;
}
</style>