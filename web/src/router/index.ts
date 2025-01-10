import { createRouter, createWebHistory } from 'vue-router'
import Home from  '@/views/Home.vue'
import Login from '@/views/login/Login.vue'
import EchartsComponent from '@/views/chart/SalesData.vue'

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

    }

    
]

const router = createRouter({
    history:createWebHistory(), //跳转方式
    routes:routes
})

export default router
