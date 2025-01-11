import { createRouter, createWebHistory } from 'vue-router'
import Home from  '@/views/Home.vue'
import Login from '@/views/login/Login.vue'
import EchartsComponent from '@/views/chart/SalesData.vue'
import ModifyPersonalData from '@/views/admin/PersonInfo.vue'
import ChangePassword from '@/views/admin/ChangePassword.vue'
import CancelAccount from '@/views/admin/CancelAccount.vue'

const  routes = [ 
    {
        path:'/',
        name:"home",
        component:Home
    },
    {
        path:'/login',
        name:"login",
        component:Login

    },
    {
        path:'/chart',
        name:"chart",
        component:EchartsComponent
    },
    {
        path:'/ModifyPersonalData',
        name:"ModifyPersonalData",
        component:ModifyPersonalData
    },
    {
        path:'/ChangePassword',
        name:"ChangePassword",
        component:ChangePassword
    },
    {
        path:'/CancelAccount',
        name:"CancelAccount",
        component:CancelAccount
    }

]

const router = createRouter({
    history:createWebHistory(), //跳转方式
    routes:routes
})

export default router
