<template>
    <div class="signin-div">
        <div class="loginPart">
            <div class="header">
                
                <div class="label">
                    <h2>用户登录</h2>
                </div>
                <div class="close-button">
                    <el-button key="x" type="danger" text @click="close">x</el-button>
                </div>
            </div>
            <div class="form">
                <el-form :model="siginForm" :rules="rules" label-width="100px" style="transform: translate(-30px)">
                    <el-form-item label="邮箱" prop="email">
                        <el-input v-model="siginForm.email" placeholder="请输入邮箱" clearable></el-input>
                    </el-form-item>
                    <el-form-item label="密码" prop="password">
                        <el-input type="password" v-model="siginForm.password" placeholder="请输入密码" show-password clearable></el-input>
                    </el-form-item>
                    <el-button class="btn" type="primary" @click="login">登陆</el-button>
                    <div style="text-align: right; transform: translate(0, 30px)">
                        <el-link type="danger" style="margin-right: 140px" >忘记密码？</el-link>
                        <el-link type="warning" @click="showLoginForm.showSignUpForm">没有账号？去注册</el-link>
                    </div>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts" name="SignIn">
import { reactive, defineEmits } from 'vue';
import { useLoginForm } from '@/store/home';
import axios from 'axios';
import CryptoJS from 'crypto-js';

const showLoginForm = useLoginForm();
const emit = defineEmits(['close']); 

const siginForm = reactive({
    email: "",
    password: "",
});

const Result = reactive({
    show:false,
    email: '',
    password: '',
    success: '',
    verify_code: '',
})

const rules = {
    email: [
     
    ],
    password: [
    ]
};

const login = async () => {
    console.log("发送登录请求");
    const fromData = siginForm;

    //对密码进行加密
    const encryptedPassword = CryptoJS.MD5(fromData.password).toString();
    fromData.password = encryptedPassword;

    try {
        const response = await axios.post('127.0.0.1:8000/register_user', fromData, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }
};

const close = () => {
    emit('close'); 
};
</script>

<style lang="scss" scoped>
.signin-div {
    position: fixed;
    top: 20%;
    right: 400px;
    width: 450px;
    height: 600px;
}

.loginPart {
    width: 450px;
    height: 300px;
    background: rgba(32, 84, 182, 0.1);
    box-sizing: border-box;
    box-shadow: 0px 5px 25px rgba(0, 0, 0, 0.5);
    border-radius: 15px;
    padding: 20px; 
}

.header {
    display: flex; 
    align-items: center; 
    justify-content: space-between;
    width: 100%;
    margin-bottom: 20px;
}

.close-button {
    cursor: pointer;
    margin-right: 10px;
}

.label {
    flex: 1; 
    text-align: center;
}

.form {
    width: 100%;
}

.btn {
    transform: translate(225px);
    width: 80px;
    height: 40px;
    font-size: 15px;
}

h2 {
    margin: 0; /* 去掉默认的 margin */
    padding: 0;
    color: #000;
    text-align: center;
}
</style>
