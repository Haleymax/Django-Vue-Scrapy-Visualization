import axios from 'axios';
import { da } from 'element-plus/es/locales.mjs';

interface LoginData {
    email: string;
    password: string;
}

interface LoginResponse {
    status: number;
    message: string;
}

const API_URL = 'http://127.0.0.1:8000/login';

export const login = async (data: LoginData): Promise<LoginResponse> => {
    try {
        const params = new URLSearchParams();
        params.append('email', data.email);
        params.append('password', data.password);

        const response = await axios.post(API_URL, params, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });
        console.log('登录请求发送成功', response.data);
        return response.data;
    } catch (error) {
        if (axios.isAxiosError(error)) {
            console.log('登录请求发送失败', error.response?.data || error.message);
        } else {
            console.log('未知错误', error);
        }
        return { status: 500, message: '登录请求发送失败' };
    }
};