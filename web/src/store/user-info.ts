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
                msg:"dasdasdasdas",
                type:"danger"
            },
            password:{
                msg:"asdasdasdasdasdas",
                type:"danger",
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
                msg:"1111111111111111111",
                type:"danger",
            },
            password:{
                msg:"22222222222222222222",
                type:"danger",
            },
            confirmpassword:{
                msg:"33333333333333333333333333",
                type:"danger",
            },
            verify_code:{
                msg:"444444444444444444444444",
                type:"danger",
            },
        }
    });

    return {
        siginForm,
        sigupForm
    }

})