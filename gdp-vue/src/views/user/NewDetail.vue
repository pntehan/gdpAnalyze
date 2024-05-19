<template>
  <div class="article-detail">
    <div class="back-button" @click="goBack">
      <el-icon><Back /></el-icon>
      <span>返回</span>
    </div>
    <el-card style="margin-bottom: 30px;">
      <img :src="'data:image/jpeg;base64,'+article.cover" class="article-cover" />
      <h1 class="article-title">{{ article.title }}</h1>
      <div class="article-meta">
        <span>发布时间: {{ article.up_time }}</span>
      </div>
      <div class="article-content" v-for="p in article.content" :key="p">
        <p>{{ p }}</p>
      </div>
      <el-button :icon="Star" @click="starArticle" circle />
      <el-button class="iconfont icon-icon" @click="upStar" circle />
      <span style="margin-left: 5px;">{{ article.star }}</span>
    </el-card>
    <!-- 评论区域 -->
    <el-card style="margin-bottom: 30px;">
      <h3>评论区</h3>
      <div style="max-height: 400px; overflow-y: auto;">
        <el-list>
          <el-list-item v-for="(comment, index) in comments" :key="index" style="margin-bottom: 10px;">
            <el-card>
              <div class="comment-header">
                <span class="comment-author">{{ comment.name }}</span>
                <span class="comment-time">{{ comment.up_time }}</span>
              </div>
              <div class="comment-body">{{ comment.content }}</div>
            </el-card>
          </el-list-item>
        </el-list>
      </div>
      <h3>请评论</h3>
      <el-input
        type="textarea"
        :rows="4"
        placeholder="输入您的评论..."
        v-model="newComment"
      ></el-input>
      <el-button type="primary" @click="submitComment" style="margin-top: 10px"
        >提交评论</el-button
      >
    </el-card>
  </div>
</template>

<script setup>
import { Star } from '@element-plus/icons-vue'
</script>

<script>
import { Back } from '@element-plus/icons-vue'
import { getArticle, addStarArticle, goodArticle, initArticleCmt, addArticleCmt } from '@/api/Student.js'
import { ElMessage } from 'element-plus';

export default {
  components: {
    Back
  },

  data() {
    return {
      maxStarNum: 0,
      article: {
        id: 0,
        title: '',
        cover: '',
        up_time: '',
        content: [],
        star: 0
      },
      comments: [], // 评论列表
      newComment: '' // 新评论内容
    }
  },

  mounted() {
    this.$emit('change-value', 'new')
    let id = this.$route.params.id
    getArticle({ id: id }).then((res) => {
      this.article.id = res.data.id
      this.article.title = res.data.title
      this.article.cover = res.data.cover
      this.article.star = res.data.star
      // 将字符串转换为 Date 对象
      let dateTime = new Date(res.data.up_time)
      // 获取年月日
      let year = dateTime.getFullYear()
      let month = String(dateTime.getMonth() + 1).padStart(2, '0')
      let day = String(dateTime.getDate()).padStart(2, '0')
      // 获取小时分钟秒
      let hours = String(dateTime.getHours()).padStart(2, '0')
      let minutes = String(dateTime.getMinutes()).padStart(2, '0')
      let seconds = String(dateTime.getSeconds()).padStart(2, '0')
      this.article.up_time = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
      this.article.content = res.data.content.split('&&')
    })
    // 初始化评论区
    initArticleCmt({article_id: id}).then((res) => {
      this.comments = res.data
      this.comments.sort((a, b) => new Date(b.up_time) - new Date(a.up_time))
    })
  },

  methods: {
    goBack() {
      this.$router.go(-1)
    },

    starArticle() {
      let user_info = JSON.parse(localStorage.getItem('user_info'))
      let params = {
        student_id: user_info.id,
        article_id: this.article.id
      }
      addStarArticle(params).then((res) => {
        if (res.status == 200) {
          ElMessage.success('您已成功收藏该文章~')
        }
        else {
          ElMessage.warning('您以及收藏过该文章了哦~')
        }
      })
    },

    upStar() {
      if (this.maxStarNum >= 1) {
        ElMessage.warning('您已经点过赞了~')
        return
      }
      let params = {article_id: this.article.id, star: this.article.star+1}
      goodArticle(params).then((res) => {
        if (res.status == 200) {
          ElMessage.success('谢谢点赞~')
          this.article.star = this.article.star + 1
          this.maxStarNum++
        }
      })
    },

    submitComment() {
      // 提交评论
      let user_info = JSON.parse(localStorage.getItem('user_info'))
      let params = {
        article_id: this.article.id,
        student_id: user_info.id,
        content: this.newComment
      }
      addArticleCmt(params).then((res) => {
        ElMessage.success('评论成功~')
        this.comments = res.data
        this.comments.sort((a, b) => new Date(b.up_time) - new Date(a.up_time))
      })
    }
  }
}
</script>

<style scoped>
.article-detail {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.back-button {
  display: flex;
  align-items: pointer;
  margin-bottom: 20px;
}

.back-button i {
  margin-right: 5px;
}

.article-cover {
  width: 100%;
  max-height: 400px;
  object-fit: cover;
  border-radius: 4px;
  margin-bottom: 20px;
}

.article-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.article-meta {
  font-size: 14px;
  color: #666;
  margin-bottom: 20px;
}

.article-meta span {
  margin-right: 10px;
}

.article-content {
  font-size: 16px;
  line-height: 1.6;
}
/* 评论区样式 */
.comment-header {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  color: #666;
  margin-bottom: 5px;
}

.comment-author {
  font-weight: bold;
}

.comment-time {
  color: #999;
}

.comment-body {
  font-size: 16px;
  line-height: 1.5;
}
</style>