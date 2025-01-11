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
                            <Avatar/>
                            <template #dropdown>
                                <DropdownMenu></DropdownMenu>
                            </template>
                        </el-dropdown>
                    </el-col>
                </el-row>
            </el-header>
            <el-container>
                <el-aside width="200px">
                    <Menu @navigate="handleClick"></Menu>
                </el-aside>
                <el-main>
                    <div class="main-content">
                        <RouterView></RouterView>
                    </div>
                </el-main>
            </el-container>
        </el-container>
    </div>

    <div v-if="showLoginForm.isLoginFormVisible" class="modal-overlay">
        <div>
            <SignIn @close="showLoginForm.hideLoginForm" />
        </div>
    </div>

    <div v-if="showLoginForm.isSignUpFormVisible" class="modal-overlay">
        <div>
            <SignUp @close="showLoginForm.hideLoginForm" />
        </div>
    </div>

    <div v-if="showLoginForm.isRetrievePassword" class="modal-overlay">
        <div>
            <RetrievePassword @close="showLoginForm.hideLoginForm" />
        </div>
    </div>
</template>

<script setup lang="ts" name='Home'>
import { ElMessage } from 'element-plus'
import Menu from '@/components/Menu.vue'
import DropdownMenu from '@/components/DropdownMenu.vue'
import Avatar from '@/components/Avatar.vue'
import {useLoginForm} from '@/store/home'
import SignIn from '@/views/login/sign_in.vue'
import SignUp from '@/views/login/sign_up.vue'
import RetrievePassword from './login/RetrievePassword.vue'
import { useRouter } from 'vue-router';
const router = useRouter();

const showLoginForm = useLoginForm()

const handleCommand = (command: string | number | object) => {
    ElMessage(`click on item ${command}`)
}

const handleClick = (path: string) => {
    console.log(path);
    if(path) {
        router.push(path)
    }
};

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

.modal-content {
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    
}

.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(5px);
    z-index: 1000;
}

.main-content {
    height: 950px;
    padding: 20px;
}
</style>
