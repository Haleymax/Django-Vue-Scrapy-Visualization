import fs from 'fs';
import path from 'path';


interface AppConfig {
    serverHost: string;
    serverPort: string;
}


export const readConfig = (): AppConfig => {
    const configFilePath = path.join(process.cwd(), 'config.json');
    try {
        const configFileContent = fs.readConfigSync(configFilePath, 'utf8')
        const config: AppConfig = JSON.parse(configFileContent);
        return config;
    } catch (error) {
        console.log('read config file error: ', error);
        return {
            serverHost:"127.0.0.1",
            serverPort:"8000",
        }
    }
}