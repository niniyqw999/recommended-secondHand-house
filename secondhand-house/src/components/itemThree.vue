<template>
  <div>
    <div class="chart" ref="myEcharts"></div>
  </div>
</template>
  
<script setup>
import { onMounted, ref } from "vue";
import * as echarts from "echarts";
import houseStore from "../store/house";

const house = houseStore();
let myEcharts = ref();
let data = house.hosplayData;
data.forEach(obj => {
  let keys = Object.keys(obj);
  let newKeys = keys.map(key => {
    if (key === 'hosplay') {
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
  let myChart = echarts.init(myEcharts.value)
  myChart.setOption({
    legend: {
      top: 'bottom'
    },
    tooltip: {
      show: true
    },
    title: {
    text: '二手房装修类型分布',
  },
    series: [
      {
        type: 'pie',
        data: data,
        radius: [10, 100],
        center: ['50%', '45%'],
        roseType: 'area',
        itemStyle: {
          borderRadius: 10
        }
      }
    ]
  })
})
</script>
  
<style lang="scss" scoped>
.chart {
  height: 4.5rem;
}
</style>