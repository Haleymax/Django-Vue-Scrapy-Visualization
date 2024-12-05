import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useLoginForm = defineStore('loginForm', () => {
    
    // 控制是否显示登录框
    const isLoginFormVisible = ref(false);

    // 控制是否显示注册框
    const isSignUpFormVisible = ref(false);

    // 显示登录框
    const showLoginForm = () => {
        isLoginFormVisible.value = true;
        isSignUpFormVisible.value = false;
    };

    // 隐藏登录框
    const hideLoginForm = () => {
        isLoginFormVisible.value = false;
        isSignUpFormVisible.value = false;
    };

    // 显示注册框
    const showSignUpForm = () => {
        isSignUpFormVisible.value = true;
        isLoginFormVisible.value = false;
    };


    return {
        isLoginFormVisible,
        isSignUpFormVisible,
        showLoginForm,
        hideLoginForm,
        showSignUpForm,
    };
});
