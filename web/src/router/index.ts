import { createRouter, createWebHistory } from 'vue-router'
import Home from  '@/views/Home.vue'
import Login from '@/views/login/Login.vue'

const  routes = [ 
    {
        path:'/home',
        name:"home",
        component:Home
    },
    {
        path:'/',
        name:"login",
        component:Login

    }
    
]

const router = createRouter({
    history:createWebHistory(), //跳转方式
    routes:routes
})

export default router
