<template>
  <div>
    <div class="chart" ref="myEcharts"></div>
  </div>
</template>
  
<script setup>
import { onMounted, ref } from "vue";
import * as echarts from "echarts";

let myEcharts = ref();
let data = [
  { value: 0.35, name: "精装" },
  { value: 0.23, name: "简装" },
  { value: 0.25, name: "毛胚" },
  { value: 0.17, name: "其他" },
];

onMounted(() => {
  let myChart = echarts.init(myEcharts.value);
  myChart.setOption({
    tooltip: {
      trigger: "item",
    },
    legend: {
      top: "5%",
      left: "center",
    },
    title: {
          text: "二手房源装修分布",
        },
    series: [
      {
        name: "Access From",
        type: "pie",
        radius: ["40%", "70%"],
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
            fontSize: 40,
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