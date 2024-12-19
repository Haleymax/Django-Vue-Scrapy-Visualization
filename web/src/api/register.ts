import axios from 'axios';

interface VerificationData {
    email: string;
    use_type: string;
}

interface ResponseData {
    status: number;
    message: string;
}

//发送验证码
export const sendVerificationCode = async (data: VerificationData): Promise<ResponseData> => {
    try {
        const params = new URLSearchParams();
        params.append('user_email', data.email);
        params.append('use_type', data.use_type);

        const response = await axios.post('http://127.0.0.1:8000/verification_code', params, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });
        console.log('验证码发送成功！', response.data);
        return response.data;
    } catch (error) {
        if (axios.isAxiosError(error)) {
            console.log("验证码发送错误", error.response?.data || error.message);
        } else {
            console.log("未知错误", error);
        }
        return { status: 500, message: '验证码发送失败' };
    }
};