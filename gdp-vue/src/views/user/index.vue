<template>
  <div>
    <top-bar :websiteName="websiteName" :tabName="tabName" :userInfo="userInfo" />
    <router-view class="container" @change-value="handleChangeValue"></router-view>
    <bottom-bar :websiteInfo="websiteInfo" />
  </div>
</template>

<script>
import TopBar from '@/components/TopBar.vue'
import BottomBar from '@/components/BottomBar.vue'

export default {
  components: {
    TopBar,
    BottomBar,
  },

  data() {
    return {
      websiteName: '黄河流域GDP分析网站',
      tabName: 'home',
      userInfo: 'User Information',
      websiteInfo: 'Your Website Information',
      intervalId: '',
      msgNum: 0
    };
  },

  mounted() {
    this.tabName = this.$route.name
  },

  methods: {
    handleChangeValue(newValue) {
      this.tabName = newValue
    }
  }
};
</script>

<style scoped>
.container {
  margin-top: 80px;
  margin-bottom: 100px;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('@/assets/bg.jpg');
  background-size: cover;
  background-position: center;
  z-index: -1;
}

.container::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  backdrop-filter: blur(8px);
  pointer-events: none;
}
</style>
