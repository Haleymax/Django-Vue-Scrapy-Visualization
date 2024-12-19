import { defineStore } from 'pinia'
import { reactive } from 'vue'

export const useUserInfo = defineStore('UserInfo', () => {
    
    const siginForm = reactive({
        data:{
            email:'',
            password:'',
        },
        message: {
            email:{
                msg:"",
                type:""
            },
            password:{
                msg:"",
                type:"",
            }
        }
    }) 

    const sigupForm = reactive({
        data:{
            email:'',
            password:'',
            confirmpassword:'',
            verify_code:'',
        },
        message:{
            email:{
                msg:"",
                type:"",
            },
            password:{
                msg:"",
                type:"",
            },
            confirmpassword:{
                msg:"",
                type:"",
            },
            verify_code:{
                msg:"",
                type:"",
            },
        }
    });

    return {
        siginForm,
        sigupForm
    }

})