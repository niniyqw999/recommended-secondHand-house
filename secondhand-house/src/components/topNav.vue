<template>
  <el-menu
    :default-active="route.fullPath"
    class="el-menu-demo"
    mode="horizontal"
    :router="true"
  >
    <div class="logo">
      <svg class="icon" aria-hidden="true">
        <use xlink:href="#icon--fangzi"></use>
      </svg>
      <span>二手房购置推荐平台</span>
    </div>
    <el-menu-item index="/home">房源一览</el-menu-item>
    <el-menu-item index="/charts">房源可视化</el-menu-item>
    <el-menu-item index="/map">房源热力图</el-menu-item>
    <el-sub-menu>
      <template #title>推荐房源</template>
      <el-menu-item index="/recommand-a">协同过滤推荐</el-menu-item>
      <el-menu-item index="/recommand-b">基于内容推荐</el-menu-item>
    </el-sub-menu>
    <el-menu-item index="/personal">个人中心</el-menu-item>
    <div class="user">
      <img src="../assets/我的.png" v-if="!token" />
      <img src="../assets//我的蓝.png" v-if="token" />
      <span>
        <el-dropdown class="menu">
          <span>
            {{ token ? userData.userInfo.username : "游客" }}
            <el-icon>
              <arrow-down />
            </el-icon>
          </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item @click="router.push('/personal')"
                >个人中心</el-dropdown-item
              >
              <el-dropdown-item @click="router.push('/feedback')"
                >用户反馈</el-dropdown-item
              >
              <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </span>
    </div>
    <!-- <span class="us" style="font-size: 18px;">联系我们</span> -->
  </el-menu>
</template>
  
<script setup>
import { useRoute, useRouter } from "vue-router";
import userStore from "../store/user";
import { ArrowDown } from "@element-plus/icons-vue";
import { ElMessage } from "element-plus";

const userData = userStore();
const route = useRoute();
const router = useRouter();

//获取本地保存的token
let token = localStorage.getItem("token");

//点击退出登录的回调
const logout = () => {
  //判断用户是否登录-token         
  if (token) {
    userData.clearToken();
    router.go(0);
    ElMessage({
      type: "success",
      message: "退出登录成功",
    });
  } else {
    ElMessage({
      type: "error",
      message: "还没有登录",
    });
  }
};
</script>
  
<style lang="scss" scoped>
.el-menu-demo {
  display: flex;
  justify-content: space-around;
  align-items: center;
  .logo {
    display: flex;
    align-items: center;
    span {
      font-size: 18px;
    }
  }
  .icon {
    width: 40px;
    height: 40px;
  }
  .user {
    position: relative;
    img {
      position: absolute;
      width: 40px;
      height: 40px;
      top: -70%;
      left: -80%;
    }
  }
}
</style>