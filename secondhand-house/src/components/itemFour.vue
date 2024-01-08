<template>
  <div>
    <div class="chart" ref="myEcharts"></div>
  </div>
</template>
  
<script setup>
import { onMounted, ref } from 'vue';
import * as echarts from "echarts";
import houseStore from "../store/house";

const house = houseStore();
let myEcharts = ref();
let data = house.hostypeData;
data.forEach(obj => {
  let keys = Object.keys(obj);
  let newKeys = keys.map(key => {
    if (key === 'hostype') {
      return 'name';
    } else if (key === 'count') {
      return 'value';
    } else {
      return key;
    }
  });
  let newObj = Object.assign({}, ...newKeys.map((key, index) => ({[key]: obj[keys[index]]})));
  Object.assign(obj, newObj);
});

onMounted(() => {
  let myChart = echarts.init(myEcharts.value);
  myChart.setOption({
    tooltip: {
      trigger: "item",
    },
    legend: {
      top: "5%",
      left: "center"
    },
    title: {
          text: "二手房户型分布",
        },
    series: [
      {
        name: "户型",
        type: "pie",
        radius: ["10%", "70%"],
        avoidLabelOverlap: false,
        itemStyle: {
          borderRadius: 10,
          borderColor: "#fff",
          borderWidth: 2,
        },
        label: {
          show: false,
          position: "center",
        },
        emphasis: {
          label: {
            show: true,
            fontSize: 20,
            fontWeight: "bold",
          },
        },
        labelLine: {
          show: false,
        },
        data: data,
      },
    ],
  });
});
</script>
  
<style lang="scss" scoped>
.chart {
  height: 4.5rem;
}

</style>