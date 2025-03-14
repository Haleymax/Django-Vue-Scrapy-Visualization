import { defineStore } from 'pinia'

export const menuDataStore = defineStore('menuDate', {
    state() {
        return {
            menuDate: [
                {
                    id: 1,
                    name: '个人中心',
                    children: [
                        { id: 11, name: '修改个人资料', path: '/ModifyPersonalData' },
                        { id: 12, name: '修改密码', path: '/ChangePassword' },
                        { id: 13, name: '注销账号', path: '/CancelAccount' },
                    ],
                },
                {
                    id: 2,
                    name: '数据展示',
                    children: [
                        { id: 21, name: '销售数据', path: '/chart' },
                        { id: 22, name: 'Menu 2-2', path: '/menu2-2' },
                        { id: 23, name: 'Menu 2-3', path: '/menu2-3' },
                    ],
                },
                {
                    id: 3,
                    name: 'Menu 3',
                    children: [
                        { id: 31, name: 'Menu 3-1', path: '/menu3-1' },
                        { id: 32, name: 'Menu 3-2', path: '/menu3-2' },
                        { id: 33, name: 'Menu 3-3', path: '/menu3-3' },
                    ],
                },
                {
                    id: 4,
                    name: 'Menu 4',
                    path: '/menu4'
                },
            ]
        }
    }
})

