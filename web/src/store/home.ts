import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useLoginForm = defineStore('loginForm', () => {
    
    // 控制是否显示登录框
    const isLoginFormVisible = ref(false);

    // 控制是否显示注册框
    const isSignUpFormVisible = ref(false);

    // 控制显示找回密码框
    const isRetrievePassword = ref(true)

    // 显示登录框
    const showLoginForm = () => {
        isLoginFormVisible.value = true;
        isSignUpFormVisible.value = false;
        isRetrievePassword.value = false;
    };

    // 隐藏登录框
    const hideLoginForm = () => {
        isLoginFormVisible.value = false;
        isSignUpFormVisible.value = false;
        isRetrievePassword.value = false;
    };

    // 显示注册框
    const showSignUpForm = () => {
        isSignUpFormVisible.value = true;
        isLoginFormVisible.value = false;
        isRetrievePassword.value = false;
    };

    // 显示找回密码框
    const showRetrievePassword = () => {
        isRetrievePassword.value = true;
        isLoginFormVisible.value = false;
        isSignUpFormVisible.value = false;

    }

    return {
        isLoginFormVisible,
        isSignUpFormVisible,
        isRetrievePassword,
        showLoginForm,
        hideLoginForm,
        showSignUpForm,
        showRetrievePassword,
    };
});
