import {fileURLToPath, URL} from 'node:url'

import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue()],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    },
    server: {
        cors: true,
        proxy: {
            "/api": {
                target: "http://localhost:8088",
                secure: false,
                changeOrigin: true, //this one is declare for cross
                rewrite: (path) => {
                    console.log(path);
                    return path.replace(/^\/api/, '')
                }
            }
        }
    }
})