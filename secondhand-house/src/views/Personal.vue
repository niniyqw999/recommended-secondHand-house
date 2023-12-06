<template>
  <topNav></topNav>
  <el-row>
    <el-col :span="18">
      <h2 class="title">我收藏的房源</h2>
      <el-table :data="likeData" border style="width: 96%;margin: 0 2%;">
        <el-table-column prop="name" label="房源名称" align="center" />
        <el-table-column prop="region" label="房源地区" align="center" />
        <el-table-column prop="price" label="房屋价格(万元)" align="center" />
        <el-table-column prop="hostype" label="房屋户型" align="center" />
        <el-table-column prop="size" label="房屋大小(m^2)" align="center" />
        <el-table-column prop="direction" label="房屋朝向" align="center" />
        <el-table-column prop="playtype" label="装修类型" align="center" />
        <el-table-column prop="height" label="楼层高度(层数)" align="center" />
      </el-table>
    </el-col>
    <el-col :span="6">

    </el-col>
  </el-row>
</template>

<script setup>
import { ref,onMounted } from "vue";
import houseStore from '../store/house'

//引用pinia库的数据
const house = houseStore()
//存储收藏的数据
let likeData=ref([])
//挂载请求房源数据
onMounted(() => {
  //请求表格数据
  getlikeData()
})
//定义获取表格数据方法
const getlikeData = () => {
  likeData.value = house.tableData.filter(h=>h.islike===true)
}
</script>

<style lang="scss" scoped>
.title{
  color:rgb(109, 177, 246);
  font-size: 20px;
  text-align:left;
  margin: 20px;
}
</style>