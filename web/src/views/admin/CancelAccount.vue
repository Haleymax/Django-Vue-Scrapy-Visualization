<template>
    <el-form :model="form" label-width="auto" style="max-width: 600px">
        <el-form-item label="密码">
            <el-input type="password" v-model="form.user_password" placeholder="请输入密码" show-password/>
        </el-form-item>
        <el-button type="primary" @click="onSubmit">注销</el-button>
        <el-button @click="onClear">清空</el-button>
    </el-form>
</template>

<script lang="ts" setup name="CancelAccount">
import { reactive } from 'vue'

const form = reactive({
    user_password: '',
})

const onSubmit = () => {
    console.log('submit!')
}

const onClear = () => {
    form.user_password = '',
    console.log('clear!')
}


</script>