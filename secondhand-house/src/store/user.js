import { defineStore } from 'pinia'


// 定义store，名称为user
const userStore = defineStore('user', {
  // 定义state，返回一个对象
  state: () => ({
    userInfo: {},
    token: ''
  }),
  // 定义actions，返回一个对象
  actions: {
    //设置token
    setToken(token, userInfo) {
      this.token = token;
      this.userInfo = userInfo;
    },
    //清除token
    clearToken() {
      this.token = '';
      this.userInfo = {};
      localStorage.removeItem('token');
    }
  },
  // 定义getters，返回一个对象
  getters: {

  }
})

// 导出store
export default userStore