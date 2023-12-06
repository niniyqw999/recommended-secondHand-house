import { createApp } from 'vue'
import App from './App.vue'

//清除默认样式
import './style.scss'
//引入element-plus插件
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
//引入路由
import router from './router'
//引入pinia仓库
import pinia from './store'
import topNav from './components/topNav.vue'
//引入路由权限文件
import './permission'
//引入页面适应文件
import 'lib-flexible/flexible'

const app = createApp(App)
// 全局注册组件
app.component('topNav',topNav)

app.use(router).use(ElementPlus).use(pinia).mount('#app')
