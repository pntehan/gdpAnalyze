<template>
  <div class="container">
    <div>
      <h1>公告栏</h1>
    </div>
    <div class="demo-collapse" style="margin-top: 20px;">
      <el-collapse>
        <el-collapse-item v-for="item in item_list" :name="item.id" :key="item.id">
          <template #title>
            <div style="display: flex; justify-content: space-between; width: 100%;">
              <span>{{ item.title }}</span>
              <span>{{ item.up_time }}</span>
            </div>
          </template>
          <div>
            {{ item.content }}
          </div>
        </el-collapse-item>
      </el-collapse>
    </div>
    <div style="display: flex; justify-content: center;">
      <el-pagination background layout="prev, pager, next" :total="all_list.length" style="margin-top: 20px;" @current-change="pageChange" />
    </div>
  </div>
</template>

<script>
import { initAnnouncement } from '@/api/Student'

export default {
  data() {
    return {
      all_list: [],
      item_list: []
    };
  },

  mounted() {
    this.$emit('change-value', 'announcement')
    initAnnouncement().then((res) => {
      this.all_list = res.data
      this.all_list.sort((a, b) => new Date(b.up_time) - new Date(a.up_time))
      this.pageChange(1)
    })
  },

  methods: {
    pageChange(page) {
      this.item_list = []
      for (let i=0; i<10; i++) {
        let ind = (page - 1) * 10 + i
        if (ind >= this.all_list.length) {
          break
        }
        // 将字符串转换为 Date 对象
        let dateTime = new Date(this.all_list[ind].up_time)
        // 获取年月日
        let year = dateTime.getFullYear()
        let month = String(dateTime.getMonth() + 1).padStart(2, '0')
        let day = String(dateTime.getDate()).padStart(2, '0')
        // 获取小时分钟秒
        let hours = String(dateTime.getHours()).padStart(2, '0')
        let minutes = String(dateTime.getMinutes()).padStart(2, '0')
        let seconds = String(dateTime.getSeconds()).padStart(2, '0')
        this.all_list[ind].up_time = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
        this.item_list.push(this.all_list[ind])
      }
    }
  }
}
</script>

<style scoped>
.container {
  margin-left: 15%;
  margin-right: 15%;
}
</style>
