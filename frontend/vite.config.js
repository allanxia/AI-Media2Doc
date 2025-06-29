import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig(({ mode }) => {
  // 加载环境变量
  const env = loadEnv(mode, process.cwd())

  return {
    plugins: [vue()],
    server: {
      host: '0.0.0.0',
      allowedHosts: [
        'localhost',
        '127.0.0.1',
        'media2doc.tenyunnet.cn',
        '.tenyunnet.cn'
      ],
      headers: {
        'Cross-Origin-Opener-Policy': 'same-origin',
        'Cross-Origin-Embedder-Policy': 'require-corp',
        'Cross-Origin-Resource-Policy': 'same-origin'
      },
      proxy: {
        '/api': {
          target: 'https://vite-media2doc.tenyunnet.cn',
          changeOrigin: true
        },
      },
      cors: true
    },
    define: {
      'process.env': {}
    }
  }
})
