import { createRouter, createWebHistory } from 'vue-router'
import Home from  '@/views/Home.vue'

const  routes = [
	// 注意这里使用路由path:'/'，Home, 如果你在app.vue  已经加载了首页，要删除app.vue中的组件，不然会重复加载  
    {
        path:'/home',
        name:"home",
        component:Home
    }
]

const router = createRouter({
    history:createWebHistory(), //跳转方式
    routes:routes
})

export default router
