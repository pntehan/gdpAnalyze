<template>
  <div class="block text-center">
    <div class="title-header">
      <h3 @click="jumpTo">
        {{ title }}
      </h3>
    </div>
    <el-carousel height="800px" @change="changeTitle" interval="3000">
      <el-carousel-item v-for="item in itemList" :key="item.id" @click="jumpTo">
        <img class="carousel-img" :src="'data:image/jpeg;base64,'+item.cover">
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
import { initHome } from '@/api/Student.js'

export default {
  data() {
    return {
      title: '',
      id: 0,
      itemList: []
    }
  },

  mounted() {
    this.$emit('change-value', 'home')
    initHome().then((res) => {
      this.itemList = res.data
      this.title = this.itemList[0].title
      this.id = this.itemList[0].id
    })
  },

  methods: {
    changeTitle(index) {
      this.title = this.itemList[index].title
      this.id = this.itemList[index].id
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
  max-height: 100%;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
