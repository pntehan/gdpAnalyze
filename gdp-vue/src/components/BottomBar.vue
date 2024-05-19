<template>
  <div class="bottom-bar">
    <p>{{ websiteInfo }}</p>
  </div>
</template>

<script>
export default {
  props: {
    websiteInfo: String,
  },
};
</script>

<style scoped>
.bottom-bar {
  position: fixed; /* 固定在底部 */
  bottom: 0; /* 距离底部的距离为0 */
  left: 0; /* 距离左侧的距离为0，如果需要居中可以使用margin: 0 auto; */
  width: 100%; /* 宽度100% */
  background-color: #6d6060; /* 设置背景颜色 */
  color: #fff; /* 设置文字颜色 */
  text-align: center;
  padding: 10px 0;
}

.bottom-bar p {
  margin: 0;
}
</style>
  