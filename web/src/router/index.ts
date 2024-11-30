import { createRouter, createWebHistory } from 'vue-router'
import Home from  '@/views/Home.vue'
import Login from '@/views/login/Login.vue'
import component from 'element-plus/es/components/tree-select/src/tree-select-option.mjs'

const  routes = [ 
    {
        path:'/',
        name:"home",
        component:Home
    },
    {
        path:'/login',
        name:"login",
        component:Login,
        children:[
            {
                
            }
        ]

    }
    
]

const router = createRouter({
    history:createWebHistory(), //跳转方式
    routes:routes
})

export default router
