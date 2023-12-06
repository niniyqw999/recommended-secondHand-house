<template>
    <topNav></topNav>
    <div ref="mymap" id="mymap">
    </div>
</template>
  
<script setup>
import { onMounted, ref } from 'vue';
import * as echarts from 'echarts';
import 'echarts/extension/bmap/bmap';

//获取dom元素
const mymap = ref()
//存储热力图数据
let points = [
    [114.29857211111, 30.5843651561,1],
    [114.29857215465, 30.5843553156,1],
    [114.29857216521, 30.58435511954,1],
    [114.298572122651, 30.5843551154,1],
];
//定义图表配置项
let option = {
    width: '100%',
    height: '100%',
    animation: false,
    bmap: {
        center: [114.29857211111, 30.58435511111],
        zoom: 14,
        roam: true
    },
    visualMap: {
        show: false,
        top: 'top',
        min: 0,
        max: 5,
        seriesIndex: 0,
        calculable: true,
        inRange: {
            color: ['blue', 'blue', 'green', 'yellow', 'red']
        }
    },
    series: [
        {
            type: 'heatmap',
            coordinateSystem: 'bmap',
            data: points,
            pointSize: 5,
            blurSize: 6,
        }
    ]
}

onMounted(() => {
    //获取图表信息
    getChart()
})
//获取图标信息的回调
const getChart = () => {
    //初始化图标实例
    const myChart = echarts.init(mymap.value);
    //图表配置项配置
    myChart.setOption(option);
    // // 添加百度地图插件
    // const bmap = myChart.getModel().getComponent('bmap').getBMap();
    // bmap.addControl(new BMap.MapTypeControl());
    // bmap.setSize(new BMap.Size(1300, 700));
}
</script>
  
<style lang="scss" scoped></style>