import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import { ElMessage } from 'element-plus'
import 'element-plus/dist/index.css'
import './assets/iconfont.css'

const app = createApp(App)
app.config.globalProperties.$message = ElMessage;
app.use(store)
app.use(router)
app.use(ElementPlus)
app.mount('#app')

