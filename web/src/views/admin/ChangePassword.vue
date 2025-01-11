<template>
    <el-form :model="form" label-width="auto" style="max-width: 600px">
        <el-form-item label="原密码">
            <el-input type="password" v-model="form.user_password" placeholder="请输入原密码" show-password/>
        </el-form-item>
        <el-form-item label="新密码">
            <el-input type="password" v-model="form.user_new_password" placeholder="请输入新密码" show-password/>
        </el-form-item>
        <el-form-item label="确认新密码">
            <el-input type="password" v-model="form.confirm_password" placeholder="请再次输入新密码" show-password/>
        </el-form-item>
        <el-button type="primary" @click="onSubmit">修改</el-button>
        <el-button @click="onClear">清空</el-button>
    </el-form>
</template>

<script lang="ts" setup name="ChangePassword">
import { reactive } from 'vue'

const form = reactive({
    user_password: '',
    user_new_password: '',
    confirm_password:'',
})

const onSubmit = () => {
    console.log('submit!')
}

const onClear = () => {
    form.user_password = '',
    form.user_new_password = '',
    form.confirm_password = '',
    console.log('clear!')
}


</script>