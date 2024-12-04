import {defineStore} from 'pinia'
import { ref } from 'vue'

export const useLoginForm = defineStore('showLoginForm', () => {
    
    //设置变量控制是否显示登录框
    let isShow = ref(false)

    const set_false = () => {
        isShow.value = false;
    }

    const set_true = () => {
        isShow.value = true;
    }
    
    return {isShow, set_false, set_true};
})