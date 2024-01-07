import { defineStore } from 'pinia'


const houseStore = defineStore('house', {
  state: () => ({
    //用户收藏房源的id集合
    likedData: [],
    //渲染可视化的数据
    averagePrice: [],
    maxPrice: [],
    minPrice: [],
    hostypeData: [],
    hospalyData: [],
  }),
  actions: {

  },
  getters: {

  }
})

export default houseStore