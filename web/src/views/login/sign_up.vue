<template>
    <div class="signin-div">
        <div class="loginPart">
            <div class="header">

                <div class="label">
                    <h2>用户注册</h2>
                </div>
                <div class="close-button">
                    <el-button key="x" type="danger" text @click="close">x</el-button>
                </div>
            </div>
            <div class="form">
                <el-form :model="siginForm" label-width="100px" style="transform: translate(-30px)">
                    <el-form-item label="邮箱" prop="email">
                        <el-input class="input-box" v-model="siginForm.email" placeholder="请输入邮箱" clearable></el-input>
                    </el-form-item>
                    <el-form-item label="密码" prop="password">
                        <el-input class="input-box" type="password" v-model="siginForm.password" placeholder="请输入密码"
                            show-password clearable></el-input>
                    </el-form-item>
                    <el-form-item label="确认密码" prop="confirmPassword">
                        <el-input class="input-box" type="password" v-model="siginForm.confirmPassword"
                            placeholder="请再次输入密码" show-password clearable></el-input>
                    </el-form-item>
                    <el-form-item label="验证码" prop="code">
                        <el-input style="width: 100px;" v-model="siginForm.code" placeholder="验证码" clearable></el-input>
                        <div>验证码图片</div>
                    </el-form-item>
                    <el-button class="btn" type="primary" @click="login">注册</el-button>
                    <div style="text-align: right; transform: translate(0, 30px)">
                        <el-link type="warning" style="margin-right: 140px">已有账号？去登录</el-link>
                    </div>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts" name="SignUp">
import { reactive } from 'vue';
import { ElForm } from 'element-plus'; // 导入ElForm类型（如果需要类型检查）
import Login from './Login.vue';

const emit = defineEmits(['close']); 


const siginForm = reactive({
    email: "",
    password: "",
    confirmPassword: "",
    code: "",
});

const rules = {
    email: [
        { required: true, message: '请输入邮箱', trigger: 'blur' },
        { type: 'email', message: '请输入正确的邮箱格式', trigger: ['blur', 'change'] }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' }
    ],
    confirmPassword: [
        { required: true, message: '请确认密码', trigger: 'blur' }
    ],
    code: [
        { required: true, message: '请输入验证码', trigger: 'blur' }
    ]
};

//发送注册请求
const login = async () => {
    console.log("发送注册请求");
}
</script>

<style lang="scss" scoped>
.signin-div {
    position: fixed;
    top: 20%;
    right: 400px;
    width: 450px;
    height: 800px;
}

.label {
    flex: 1;
    text-align: center;
}


.form {
    width: 100%;
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

.loginPart {
    width: 450px;
    height: 500px;
    background: rgba(32, 84, 182, 0.1);
    box-sizing: border-box;
    box-shadow: 0px 5px 25px rgba(0, 0, 0, 0.5);
    border-radius: 15px;
    padding: 20px; // 添加内边距
}

.btn {
    transform: translate(225px);
    width: 80px;
    height: 40px;
    font-size: 15px;
}

.input-box {
    width: 100%; // 使输入框占满整个可用宽度
}

h2 {
    margin: 50px 0;
    padding: 0;
    color: #000;
    text-align: center;
}
</style>
