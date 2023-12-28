<template>
  <topNav></topNav>
  <el-form :inline="true" :model="houseInfo" class="demo-form-inline">
    <el-form-item>
      <el-input v-model="houseInfo.name" placeholder="输入房源名称" clearable />
    </el-form-item>
    <el-form-item>
      <el-select v-model="houseInfo.region" placeholder="选择地区" clearable>
        <el-option
          :label="item"
          :value="item"
          v-for="item in regionOptions"
          :key="item"
        />
      </el-select>
    </el-form-item>
    <el-form-item>
      <el-select v-model="houseInfo.direction" placeholder="选择朝向" clearable>
        <el-option
          :label="item"
          :value="item"
          v-for="item in directionOptions"
          :key="item"
        />
      </el-select>
    </el-form-item>
    <el-form-item>
      <el-select v-model="houseInfo.hostype" placeholder="选择户型" clearable>
        <el-option
          :label="item"
          :value="item"
          v-for="item in hostypeOptions"
          :key="item"
        />
      </el-select>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" plain @click="searchData(houseInfo)"
        >查询</el-button
      >
    </el-form-item>
    <el-form-item>
      <el-button type="warning" plain @click="reset">重置</el-button>
    </el-form-item>
  </el-form>
  <el-table
    :data="tableData"
    border
    style="width: 96%; margin: 0 2%; overflow: hidden"
    v-loading="loading"
    element-loading-text="正在爬取房源数据，请耐心等待..."
    :element-loading-spinner="svg"
    element-loading-svg-view-box="-10, -10, 50, 50"
    element-loading-background="rgba(122, 122, 122, 0.8)"
    v-infinite-scroll="loadData"
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
          :class="scope.row.islike ? 'iconfont1 ' : ''"
          @click="addLike(scope.row)"
          class="iconfont icon-shoucang iconfont2"
        ></i>
        <a :href="scope.row.detail" target="_blank">查看详情</a>
      </template>
    </el-table-column>
  </el-table>
  <span class="tips">滚动加载更多房源数据</span>
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";
import houseStore from "../store/house";
import { getHouseData } from "../untils/request";
import { ElMessage } from "element-plus";

//设置loading
const loading = ref(true);
const svg = `
        <path class="path" d="
          M 30 15
          L 28 17
          M 25.61 25.61
          A 15 15, 0, 0, 1, 15 30
          A 15 15, 0, 1, 1, 27.99 7.5
          L 15 15
        " style="stroke-width: 4px; fill: rgba(0, 0, 0, 0)"/>
      `;
//引用pinia库的数据
const house = houseStore();
//存储地区数据
let regionOptions = ref([]);
//存储朝向数据
let directionOptions = ref([]);
//存储户型数据
let hostypeOptions = ref([]);
//存储需要搜索的房源信息
let houseInfo = reactive({
  name: "", //名称
  region: "", //地区
  direction: "", //朝向
  hostype: "", //户型
});
//存储表格信息
let tableData = ref([]);
//表格长度
let tableLength = ref(10);
//挂载请求房源数据
onMounted(() => {
  //请求表格数据
  getTableData();
});
//定义获取表格数据方法
const getTableData = () => {
  getHouseData(tableLength.value).then((res) => {
    // console.log(res)
    if (res.code == 200) {
      ElMessage({
        message: "爬取数据成功",
        type: "success",
        grouping: true,
      });
      tableData.value = res.houseData;
      // console.log(tableData.value);
      //请求地区数据
      getRegion();
      //请求朝向数据
      getDeriction();
      //请求户型数据
      getHostype();
      //quire数据后关闭loading
      loading.value = false;
    } else {
      ElMessage({
        message: "爬取数据失败",
        type: "error",
      });
    }
  });
};
//定义表格下拉滚动获取数据的方法
const loadData = () => {
  tableLength.value += 2;
  getTableData();
  //请求地区数据
  getRegion();
  //请求朝向数据
  getDeriction();
  //请求户型数据
  getHostype();
};
//定义获取地区数据方法
const getRegion = () => {
  // regionOptions.value = house.regionOptions;
  let regions = tableData.value.map((item) => item.region);
  regionOptions.value = [...new Set(regions)];
};
//定义获取朝向数据的方法
const getDeriction = () => {
  // directionOptions.value = house.directionOptions;
  let directions = tableData.value.map((item) => item.direction);
  directionOptions.value = [...new Set(directions)];
};
//定义获取户型数据的方法
const getHostype = () => {
  // hostypeOptions.value = house.hostypeOptions;
  let hostypes = tableData.value.map((item) => item.hostype);
  hostypeOptions.value = [...new Set(hostypes)];
};
//按下查询按钮的回调
const searchData = (form) => {
  house.search(form);
  tableData.value = house.searchData;
};

//按下重置按钮的回调
const reset = () => {
  Object.assign(houseInfo, {
    name: "", //名称
    region: "", //地区
    direction: "", //朝向
    hostype: "", //户型
  });
  //请求表格数据
  getTableData();
};
//点击收藏的图标的回调
const addLike = (row) => {
  //改变仓库内是否收藏的状态
  house.changeLike(row.name);
  console.log(row.islike);
};
</script>

<style lang="scss" scoped>
.demo-form-inline {
  margin: 20px 50px;

  .el-input {
    --el-input-width: 200px;
  }
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
.tips {
  font-size: 30px;
  color: #909399;
  position: relative;
  opacity: 0.3;
  left: 40%;
}
</style>