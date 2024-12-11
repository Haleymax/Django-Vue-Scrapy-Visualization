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
                <el-form :model="user_info.siginForm.data" :rules="rules" label-width="100px"
                    style="transform: translate(-30px)">
                    <el-form-item label="邮箱" prop="email">
                        <el-input v-model="user_info.siginForm.data.email" placeholder="请输入邮箱" clearable></el-input>
                    </el-form-item>
                    <span class="message-container">
                        <el-text v-if="user_info.siginForm.message.email.msg"
                            :type=user_info.siginForm.message.email.type>{{ user_info.siginForm.message.email.msg
                            }}</el-text>
                    </span>

                    <el-form-item label="密码" prop="password">
                        <el-input type="password" v-model="user_info.siginForm.data.password" placeholder="请输入密码"
                            show-password clearable></el-input>
                    </el-form-item>
                    <span class="message-container2">
                        <el-text v-if="user_info.siginForm.message.password.msg"
                            :type=user_info.siginForm.message.password.type>{{ user_info.siginForm.message.password.msg
                            }}</el-text>
                    </span>
                    <el-button class="btn" type="primary" @click="login">登陆</el-button>
                    <div style="text-align: right; transform: translate(0, 30px)">
                        <el-link type="danger" style="margin-right: 140px">忘记密码？</el-link>
                        <el-link type="warning" @click="showLoginForm.showSignUpForm">没有账号？去注册</el-link>
                    </div>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts" name="SignIn">
import { reactive, defineEmits, watch } from 'vue';
import { useLoginForm } from '@/store/home';
import { useUserInfo } from '@/store/user-info';
import axios from 'axios';
import CryptoJS from 'crypto-js';

const showLoginForm = useLoginForm();
const user_info = useUserInfo()

const emit = defineEmits(['close']);


const rules = {
    email: [

    ],
    password: [
    ]
};

watch(user_info.siginForm.data, () => {
    console.log("输入框发生变化，清空提示消息")
    user_info.siginForm.message.email.msg = ""
    user_info.siginForm.message.password.msg = ""
}, {deep: true});

const login = async () => {
    console.log("发送登录请求");
    const fromData = user_info.siginForm.data;

    // //对密码进行加密
    // const encryptedPassword = CryptoJS.MD5(fromData.password).toString();
    // fromData.password = encryptedPassword;

    // try {
    //     const response = await axios.post('127.0.0.1:8000/register_user', fromData, {
    //         headers: {
    //             'Content-Type': 'application/json'
    //         }
    //     })
    // }
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

.message-container {
    position: absolute;
    top: 26px;
    left: 110px;
}

.message-container2 {
    position: absolute;
    top: 79px;
    /* 距离父元素顶部20px */
    left: 110px;
    /* 距离父元素左侧30px */
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
    margin: 0;
    /* 去掉默认的 margin */
    padding: 0;
    color: #000;
    text-align: center;
}
</style>
