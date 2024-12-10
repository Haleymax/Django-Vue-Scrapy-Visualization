import { defineStore } from 'pinia'
import { reactive } from 'vue'

export const useUserInfo = defineStore('UserInfo', () => {
    
    const siginForm = reactive({
        data:{
            email:'',
            password:'',
        },
        message: {
            email:'',
            password:'',
        }
    }) 

    const sigupForm = reactive({
        data:{
            email:'',
            password:'',
            verify_code:'',
        },
        message:{
            email:'',
            password:'',
            verify_code:'',
        }
    });

    return {
        siginForm,
        sigupForm
    }

})