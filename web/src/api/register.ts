import axios from 'axios';

//发送验证码
export const sendVerificationCode = async (userId:string):Promise<void> => {
    try {
        const respone = await axios.post('后端验证码接口，还没有实现后面补起来', {userId});
        console.log('验证码发送成功！', respone.data);
    } catch(error){
        console.log("验证码发送错误", error);
    };    
};