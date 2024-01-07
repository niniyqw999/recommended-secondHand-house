<template>
  <div>
    <div class="chart" ref="oneChart">图表的容器</div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import * as echarts from 'echarts';
import houseStore from "../store/house";

const house = houseStore()
let oneChart = ref()
let xdata = house.averagePrice.map(item => item.region)
let ydata = house.averagePrice.map(item => item.price)
onMounted(() => {
  let myChart = echarts.init(oneChart.value);
  myChart.setOption({
    grid: {
      top: '3%',
      left: '3%',
      right: '6%',
      bottom: '0%',
      containLabel: true
    },
    title: {
    text: '各区房价平均价',
  },
    xAxis: {
      type: "category",
      data: xdata,
    },
    yAxis: {
      type: "value",
    },
    tooltip: {
      show: true
    },
    series: [
      {
        data: ydata,
        type: "bar",
        itemStyle: {
          barBorderRadius: [20, 20, 0, 0],
          color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
            {
              offset: 0,
              color: "#005eaa",
            },
            {
              offset: 0.5,
              color: "#339ca8",
            },
            {
              offset: 1,
              color: "#cda819",
            },
          ]),
        },
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