<template>
    <div class="signin-div">
        <div class="loginPart">
            <div class="label">
                <h2>用户登录</h2>
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
                        <el-link type="danger" style="margin-right: 140px">忘记密码？</el-link>
                        <el-link type="warning" @click="close">没有账号？去注册</el-link>
                    </div>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts" name="SignIn">
import { reactive, defineEmits } from 'vue';

const emit = defineEmits(['close']); 

const siginForm = reactive({
    email: "",
    password: "",
});

const rules = {
    email: [
        { required: true, message: '请输入邮箱', trigger: 'blur' },
        { type: 'email', message: '请输入正确的邮箱格式', trigger: ['blur', 'change'] }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' }
    ]
};

const login = async () => {
    console.log("发送登录请求");

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

.label {
    position: relative;
    width: 100%;
    height: 60px;
    line-height: 60px; 
    text-align: center;
    margin-bottom: 20px; 
}

.form {
    width: 100%;
}

.loginPart {
    width: 450px;
    height: 300px;
    background: rgba(32, 84, 182, 0.1);
    box-sizing: border-box;
    box-shadow: 0px 5px 25px rgba(0, 0, 0, 0.5);
    border-radius: 15px;
}

.btn {
    transform: translate(225px);
    width: 80px;
    height: 40px;
    font-size: 15px;
}

h2 {
    margin: 50 0 50 px;
    padding: 0;
    color: #000;
    text-align: center;
}
</style>