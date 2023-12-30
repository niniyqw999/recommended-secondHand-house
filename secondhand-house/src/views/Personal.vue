<template>
  <topNav></topNav>
  <h2 class="title">我收藏的房源</h2>
  <el-table
    :data="likeData"
    border
    style="width: 96%; margin: 0 2%; overflow: hidden"
  >
    <el-table-column prop="name" label="房源名称" align="center" />
    <el-table-column prop="region" label="房源地区" align="center" />
    <el-table-column prop="price" label="房屋价格(万元)" align="center" />
    <el-table-column prop="hostype" label="房屋户型" align="center" />
    <el-table-column prop="size" label="房屋大小(m^2)" align="center" />
    <el-table-column prop="direction" label="房屋朝向" align="center" />
    <el-table-column prop="hosplay" label="装修类型" align="center" />
    <el-table-column prop="height" label="楼层高度(层数)" align="center" />
    <el-table-column label="操作" align="center">
      <template #default="scope">
        <i
          @click="addLike(scope.row)"
          class="iconfont icon-shoucang iconfont2"
        ></i>
        <a :href="scope.row.detail" target="_blank">查看详情</a>
      </template>
    </el-table-column>
  </el-table>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { getCollectData } from "../untils/request";

//存储收藏的数据
let likeData = ref([]);
//挂载请求房源数据
onMounted(() => {
  //请求表格数据
  getlikeData();
});
//定义获取表格数据方法
const getlikeData = () => {
  getCollectData().then((res) => {
    likeData.value = res.houseData;
  });
};
//点击收藏的图标的回调
const addLike = (row) => {
  //传入房源id
  addCollect(row._id.$oid).then((res) => {
    if (res.code === 200) {
      ElMessage({
        message: res.message,
        type: "success",
      });
    } else {
      ElMessage({
        message: res.message,
        type: "warning",
      });
    }
  });
};
</script>

<style lang="scss" scoped>
.title {
  color: rgb(109, 177, 246);
  font-size: 20px;
  text-align: left;
  margin: 20px;
}
.iconfont1 {
  font-size: 30px;
  cursor: pointer;
  vertical-align: middle;
  color: red;
}
.iconfont2 {
  font-size: 30px;
  cursor: pointer;
  vertical-align: middle;
}
a {
  text-decoration: none;
  color: rgb(81, 80, 80);
  &:hover {
    color: #409eff;
  }
}
</style>