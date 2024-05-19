<template>
  <div class="container">
    <div>
      <h1>心理文章乐园</h1>
    </div>
    <div class="article-list" style="margin-top: 20px;">
      <el-row :gutter="20">
        <el-col :span="8" v-for="(article, index) in articles" :key="index">
          <el-card :body-style="{ padding: '0px' }" shadow="hover" style="margin: 10px" @click="toDetail(article.id)">
            <img :src="'data:image/jpeg;base64,'+article.cover" class="article-cover" />
            <div class="article-content">
              <h3 class="article-title">{{ article.title }}</h3>
              <p class="article-excerpt">{{ article.content }}</p>
              <div class="article-meta">
                <span>{{ article.date }}</span>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import { getArticles } from '@/api/Student.js'

export default {
  data() {
    return {
      articles: []
    }
  },

  mounted() {
    this.$emit('change-value', 'new')
    getArticles().then((res) => {
      this.articles = res.data
      this.articles.sort((a, b) => new Date(b.up_time) - new Date(a.up_time))
      for(let i=0; i<this.articles.length; i++) {
        // 将字符串转换为 Date 对象
        let dateTime = new Date(this.articles[i].up_time)
        // 获取年月日
        let year = dateTime.getFullYear()
        let month = String(dateTime.getMonth() + 1).padStart(2, '0')
        let day = String(dateTime.getDate()).padStart(2, '0')
        // 获取小时分钟秒
        let hours = String(dateTime.getHours()).padStart(2, '0')
        let minutes = String(dateTime.getMinutes()).padStart(2, '0')
        let seconds = String(dateTime.getSeconds()).padStart(2, '0')
        this.articles[i].up_time = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
        this.articles[i].content = this.articles[i].content.split('&&')[0] + '......'
      }
    })
  },

  methods: {
    toDetail(id) {
      this.$router.push('/new/'+id)
    }
  }
}
</script>

<style scoped>
.container {
  margin-left: 15%;
  margin-right: 15%;
}

.article-list {
  max-width: auto;
  margin: 0 auto;
}

.article-cover {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.article-content {
  padding: 20px;
}

.article-title {
  font-size: 18px;
  margin-bottom: 10px;
}

.article-excerpt {
  color: #666;
  line-height: 1.6;
}

.article-meta {
  margin-top: 10px;
  font-size: 14px;
  color: #999;
}

.article-meta span {
  margin-right: 10px;
}
</style>