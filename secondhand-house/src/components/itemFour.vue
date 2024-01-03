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
  {value:0.15,name:'一室一厅'},
  {value:0.33,name:'二室一厅'},
  {value:0.35,name:'三室两厅'},
  {value:0.17,name:'四室两厅'},
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
    text: '二手房户型分布',
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