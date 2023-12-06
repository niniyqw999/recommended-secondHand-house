<template>
  <div>
    <div class="chart" ref="myEcharts"></div>
  </div>
</template>
  
<script setup>
import { onMounted, ref } from 'vue';
import * as echarts from 'echarts';

let myEcharts = ref()
let data = [
  {value:0.15,name:'江夏区'},
  {value:0.23,name:'汉口区'},
  {value:0.25,name:'武昌区'},
  {value:0.17,name:'南湖区'},
  {value:0.20,name:'洪山区'},
]

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
    text: '各区房源数量',
    left: 'center'
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