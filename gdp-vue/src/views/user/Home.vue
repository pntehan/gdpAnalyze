<template>
  <div class="block text-center">
    <div class="title-header">
      <h3 @click="jumpTo">
        {{ title }}
      </h3>
    </div>
    <el-carousel height="700px" @change="changeTitle" interval="3000">
      <el-carousel-item v-for="item in itemList" :key="item.id">
        <img class="carousel-img" :src="item.cover">
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      id: 0,
      itemList: [
        {title: '历史GDP统计分析', cover: require('@/assets/cover1.jpg')},
        {title: 'GDP数据可视化', cover: require('@/assets/cover2.jpg')},
        {title: '未来GDP预测', cover: require('@/assets/cover3.jpg')}
      ]
    }
  },

  mounted() {
    this.$emit('change-value', 'home')
    this.changeTitle(0)
  },

  methods: {
    changeTitle(index) {
      this.title = this.itemList[index].title
    },

    jumpTo() {
      this.$router.push('/new/'+this.id)
    }
  }
}
</script>

<style scoped>
.title-header {
  text-align: center;
  margin-top: 100px;
}

.demonstration {
  color: var(--el-text-color-secondary);
}

.el-carousel {
  text-align: center;
}

.el-carousel__item {
  width: 100%;
  height: 100%;
  background: white;
  display: flex;
  justify-content: center;
}

.carousel-img {
  max-width: 100%;
  height: 100%;
}

.el-carousel__item:nth-child(2n) {
  background-image: url('@/assets/bg_all.jpg');
}

.el-carousel__item:nth-child(2n + 1) {
  
  background-image: url('@/assets/bg_all.jpg');
}
</style>
