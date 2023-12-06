<template>
    <topNav></topNav>
    <section class="container">
      <section class="itemLeft">
        <itemPage>
          <itemOne></itemOne>
        </itemPage>
        <itemPage>
          <itemTwo></itemTwo>
        </itemPage>
      </section>
      <section class="itemRight">
        <itemPage>
          <itemThree></itemThree>
        </itemPage>
        <itemPage>
          <itemFour></itemFour>
        </itemPage>
      </section>
    </section>
</template>
  
<script setup>
import itemOne from '../components/itemOne.vue';
import itemPage from '../components/itemPage.vue';
import itemThree from '../components/itemThree.vue';
import itemTwo from '../components/itemTwo.vue';
import itemFour from '../components/itemFour.vue';
</script>
  
<style lang="scss" scoped>
  // 大容器的样式
.container {
  // 最大最小的宽度
  min-width: 1200px;
  max-width: 2048px;
  margin: 0 auto;
  padding: 0.125rem 0.125rem 0;
  // background-color: gray;
  display: flex;
  // 设置左右在页面的份数
  .itemLeft,
  .itemRight {
    flex: 5;
  }
}
</style>