<template>
  <div>
    <div class="chart" ref="myEchartsTwo">图表的容器</div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import * as echarts from 'echarts';

let myEchartsTwo = ref()
let xdata = ['东西湖小区', '汉口小区', '江夏小区', '武昌小区', '洪山小区'];
let hdata = [2.12, 2.63, 1.82, 3.6, 2.3]
let ldata = [1.2, 1.3, 1.4, 1.5, 1.6]

onMounted(() => {
  let myChart = echarts.init(myEchartsTwo.value);
  myChart.setOption({
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "cross",
        label: {
          backgroundColor: "#e6b600"
        }
      }
    },
    title: {
    text: '各区房价最高/低价',
  },
    legend: {},
    grid: {
      left: "1%",
      right: "4%",
      bottom: "1%",
      containLabel: true
    },
    xAxis: {
      type: "category",
      boundaryGap: false,
      data: xdata,
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        name: "最低房价",
        type: "line",
        data: ldata,
        smooth: true,
        showSymbol: false,
        stack: "Total",
        lineStyle: {
          width: 0,
        },
        emphasis: {
          focus: "series",
        },
        areaStyle: {
          opacity: 0.8,
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
              offset: 0,
              color: "rgb(128, 255, 165)",
            },
            {
              offset: 1,
              color: "rgb(1, 191, 236)",
            },
          ]),
        },
      },
      {
        name: "最高房价",
        type: "line",
        data: hdata,
        smooth: true,
        showSymbol: false,
        stack: "Total",
        lineStyle: {
          width: 0,
        },
        emphasis: {
          focus: "series",
        },
        areaStyle: {
          opacity: 0.8,
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            {
              offset: 0,
              color: "rgb(108, 205, 105)",
            },
            {
              offset: 1,
              color: "rgb(55, 51, 236)",
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