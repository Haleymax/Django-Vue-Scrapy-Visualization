import axios from 'axios';
import read

//发送验证码
export const sendVerificationCode = async (userId:string):Promise<void> => {
    try {
        const respone = await axios.post('', {userId});
        console.log('验证码发送成功！', respone.data);
    } catch(error){
        console.log("验证码发送错误", error);
    };    
};