<template>
    <el-form :model="form" label-width="auto" style="max-width: 600px">
        <el-form-item label="用户名">
            <el-input v-model="form.user_id" />
        </el-form-item>
        <el-form-item label="邮箱">
            <el-input v-model="form.user_email" />
        </el-form-item>
        <el-form-item label="性别">
            <el-select v-model="form.user_gender" placeholder="选择你的性别">
                <el-option label="男" value="1" />
                <el-option label="女" value="0" />
                <el-option label="保密" value="2" />
            </el-select>
        </el-form-item>
        <el-button type="primary" @click="onSubmit">修改</el-button>
        <el-button @click="onClear">清空</el-button>
    </el-form>
</template>

<script lang="ts" setup name="PersonInfo">
import { number } from 'echarts';
import { fr } from 'element-plus/es/locales.mjs';
import { reactive } from 'vue'

// do not use same name with ref
const form = reactive({
    user_id: '',
    user_email: '',
    user_gender:'',
    user_avatar: '',
})

const onSubmit = () => {
    console.log('submit!')
}

const onClear = () => {
    form.user_id = '',
    form.user_email = '',
    form.user_gender = '',
    form.user_avatar = ''
    console.log('clear!')
}


</script>