<template>
  <el-row>
    <el-col :span="10" class="left">
      <span class="title">二手房购置推荐平台</span>
      <video autoplay loop class="video">
        <source src="../assets/数据.mp4" type="video/mp4" />
      </video>
      <p class="introduce">
        通过网络爬虫采集城市二手房源数据，对数据进行清洗及分析并以可视化形式展示，帮助购房者掌握市面上二手房源的基本特征及分布情况，辅助购房者进行购房决策.
      </p>
    </el-col>
    <el-col :span="14" class="login">
      <img src="../assets/返回首页.png" alt="返回首页" class="backhome" @click="router.push('/home')"/>
      <el-card class="form" shadow="always">
        <h2>欢迎使用</h2>
        <el-form
          ref="loginFormRef"
          :model="userInfo"
          :rules="loginRules"
          label-width="85px"
          :size="formSize"
          status-icon
        >
          <el-form-item label="账号" prop="username">
            <el-input v-model="userInfo.username" />
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input v-model="userInfo.password" type="password" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="loginForm">登录</el-button>
            <router-link
              to="/register"
              style="
                text-decoration: none;
                color: rgb(109, 177, 246);
                margin-left: 20px;
              "
              >没有账号?注册一下</router-link
            >
          </el-form-item>
        </el-form>
      </el-card>
    </el-col>
  </el-row>
</template>

<script setup>
import { ElMessage } from "element-plus";
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import userStore from "../store/user";
import { login } from "../untils/request";

const router = useRouter();
//引用仓库的user数据
const userData = userStore();
//定义表单实例
let loginFormRef = ref();
//存储用户信息
let userInfo = reactive({
  username: "admin",
  password: "123456",
});
//校验规则
const loginRules = reactive({
  username: [
    {
      required: true,
      message: "请输入3到8位用户名",
      trigger: "blur",
      min: 3,
      max: 8,
    },
  ],
  password: [
    {
      required: true,
      message: "请输入6到12位密码",
      trigger: "blur",
      min:6,
      max: 12,
    },
  ],
});

//点击登录的回调
const loginForm = () => {
  loginFormRef.value
    .validate((valid) => {
      if (valid) {
        login(userInfo).then((res) => {
          if (res.code === 200) {
            userData.setToken(userInfo.username,userInfo)
            ElMessage({
              message: res.message,
              type: "success",
            });
            router.push("/home");
          }else if(res.code === 400){
        ElMessage({
          message: res.message,
          type: "error",
        });
      }
      else{
        ElMessage({
          message: res.message,
          type: "error",  
      })
      }
        });
      } 
    })
};
</script>

<style lang="scss" scoped>
.left {
  display: flex;
  align-items: center;
  flex-direction: column;
  height: 100vh;
  .title {
    font-size: 40px;
    font-weight: bold;
    color: rgb(109, 177, 246);
    -webkit-filter: url(#diff1);
    filter: url(#diff1);
    margin: 40px 0;
  }
  .video {
    height: 396px;
    width: 100%;
  }
}

.login {
  background-color: rgba(217, 219, 219, 0.4);
  display: flex;
  justify-content: center;
  align-items: center;
  .backhome {
    width: 30px;
    height: 30px;
    position: absolute;
    top: 20px;
    right: 30px;
    cursor: pointer;
  }
  .form {
    height: 300px;
    width: 400px;
    display: flex;
    align-items: center;
    border-radius: 10px;
    border: 0;
    h2 {
      font-size: 25px;
      margin: 30px 0;
      padding-left: 40px;
    }
  }
}
.introduce {
  letter-spacing: 3px;
  line-height: 25px;
  font-size: 15px;
  color: #474646;
  margin-left: 15px;
  height: 100px;
  margin-top: 50px;
}
</style>