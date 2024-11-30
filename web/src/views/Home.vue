<template>
    <div class="box">
        <el-container>
            <el-header>
                <el-row :gutter="20">
                    <el-col :span="4">
                        <div class="col1">爬虫数据可视化平台</div>
                    </el-col>
                    <el-col :span="16">
                        <div class="col2">test2</div>
                    </el-col>
                    <el-col :span="4">
                        <el-dropdown @command="handleCommand">
                            <span class="el-dropdown-link">
                                个人信息<el-icon class="el-icon--right"><arrow-down /></el-icon>
                            </span>
                            <template #dropdown>
                                <el-dropdown-menu>
                                    <el-dropdown-item command="a">Action 1</el-dropdown-item>
                                    <el-dropdown-item command="b">Action 2</el-dropdown-item>
                                    <el-dropdown-item command="c">Action 3</el-dropdown-item>
                                    <el-dropdown-item command="d" disabled>Action 4</el-dropdown-item>
                                    <el-dropdown-item command="e" divided>Action 5</el-dropdown-item>
                                </el-dropdown-menu>
                            </template>
                        </el-dropdown>
                    </el-col>
                </el-row>
            </el-header>
            <el-container>
                <el-aside width="200px">
                    <Menu></Menu>
                </el-aside>
                <el-main>Main</el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script setup lang="ts" name='Home'>
import { ElMessage } from 'element-plus'
import { ArrowDown } from '@element-plus/icons-vue'
import Menu from '@/components/Menu.vue'

const handleCommand = (command: string | number | object) => {
    ElMessage(`click on item ${command}`)
}


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

.el-row {
    align-items: center;
    vertical-align: middle;
    padding-top: 10px;
}

.el-header {
    background-color: #545c64;
}

.col1 {
    color: black;
}

.col2 {
    color: black;
}

.col3 {
    color: black;
}

.el-row:last-child {
    margin-bottom: 0;
}

.el-col {
    border-radius: 4px;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}

.example-showcase .el-dropdown-link {
    cursor: pointer;
    color: rgb(236, 19, 19);
    display: flex;
    align-items: center;
}

.userinfo {
    text-align: right;
}

.el-dropdown-link {
    color: white;
}
</style>
