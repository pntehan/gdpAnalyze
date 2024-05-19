<template>
  <div class="news-page">
    <h2>心理问题咨询区</h2>
    <div class="news-input">
      <el-form :model="newsForm" :rules="rules" ref="newsFormRef" label-width="80px">
        <el-form-item label="问题">
          <el-input v-model="newsForm.question" type="textarea" rows="5"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitNews">提交咨询</el-button>
        </el-form-item>
      </el-form>
    </div>
    <h3>咨询历史</h3>
    <div class="news-list">
      <el-table :data="newsList" style="width: 100%" max-height="400">
        <el-table-column prop="question" label="内容"></el-table-column>
        <el-table-column label="状态" width="120">
          <template #default="scope">
            <el-tag v-if="scope.row.answer" type="success">已回复</el-tag>
            <el-tag v-else type="info">未回复</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="120">
          <template #default="scope">
            <el-button type="text" @click="viewReply(scope.row)">查看回复</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <h2>留言反馈区</h2>
    <div class="message-input">
      <el-form :model="messageForm" label-width="80px">
        <el-form-item label="留言">
          <el-input v-model="messageForm.question" type="textarea" rows="5"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitMessage">提交留言</el-button>
        </el-form-item>
      </el-form>
    </div>
    <h3>反馈历史</h3>
    <div class="news-list">
      <el-table :data="msgList" style="width: 100%" max-height="400">
        <el-table-column prop="question" label="内容"></el-table-column>
        <el-table-column label="状态" width="120">
          <template #default="scope">
            <el-tag v-if="scope.row.answer" type="success">已回复</el-tag>
            <el-tag v-else type="info">未回复</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="120">
          <template #default="scope">
            <el-button type="text" @click="viewReply(scope.row)">查看回复</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <el-dialog v-model="replyDialogVisible" title="回复内容">
      <span>{{ replyContent }}</span>
    </el-dialog>
  </div>
</template>

<script>
import { defineComponent, onMounted, ref } from 'vue'
import { ElMessage } from 'element-plus'
import { initConsult, initFeedback, addConsult, addFeedback } from '@/api/Student'

export default defineComponent({
  setup(props, { emit }) {
    emit('change-value', 'consult')

    const newsForm = ref({
      question: ''
    })

    const newsFormRef = ref(null)
    const rules = {
      question: [{ required: true, message: '请输入内容', trigger: 'blur' }]
    }
    const newsList = ref([])

    const messageForm = ref({
      question: ''
    })
    const msgList = ref([])

    const replyDialogVisible = ref(false)
    const replyContent = ref('')

    onMounted(() => {
      let user_info = JSON.parse(localStorage.getItem('user_info'))
      initConsult({ student_id: user_info.id }).then((res) => {
        newsList.value = res.data
        newsList.value.sort((a, b) => new Date(b.up_time) - new Date(a.up_time))
      })
      initFeedback({ student_id: user_info.id }).then((res) => {
        msgList.value = res.data
        msgList.value.sort((a, b) => new Date(b.up_time) - new Date(a.up_time))
      })
    })

    const submitNews = () => {
      newsFormRef.value.validate(valid => {
        if (newsForm.value.question == '') {
          ElMessage.error('请填写内容后再提交~')
          return
        }
        if (valid) {
          // 提交咨询的逻辑
          let user_info = JSON.parse(localStorage.getItem('user_info'))
          let params = {
            student_id: user_info.id,
            question: newsForm.value.question
          }
          addConsult(params).then((res) => {
            newsList.value = res.data
            newsList.value.sort((a, b) => new Date(b.up_time) - new Date(a.up_time))
            ElMessage.success('成功提交咨询，请耐心等待反馈~')
            newsForm.value.question = ''
          })
        } else {
          ElMessage.error('错误提交!!')
          return false
        }
      })
    }

    const viewReply = (news) => {
      // 查看回复的逻辑
      if (news.answer) {
        replyContent.value = news.answer
        replyDialogVisible.value = true
      } else {
        ElMessage.info('管理员还未回复')
      }
    }

    const submitMessage = () => {
      // 提交留言的逻辑
      if (messageForm.value.question == '') {
        ElMessage.error('请填写内容后再提交~')
        return
      }
      // 提交咨询的逻辑
      let user_info = JSON.parse(localStorage.getItem('user_info'))
      let params = {
        student_id: user_info.id,
        question: messageForm.value.question
      }
      addFeedback(params).then((res) => {
        msgList.value = res.data
        msgList.value.sort((a, b) => new Date(b.up_time) - new Date(a.up_time))
        ElMessage.success('成功提交咨询，请耐心等待反馈~')
        messageForm.value.question = ''
      })
    }

    return {
      newsForm,
      newsFormRef,
      rules,
      newsList,
      msgList,
      messageForm,
      replyDialogVisible,
      replyContent,
      submitNews,
      viewReply,
      submitMessage
    }
  }
})
</script>

<style scoped>
.news-page {
  padding: 20px;
  margin-left: 15%;
  margin-right: 15%;
}
.news-input {
  margin-bottom: 20px;
}
.news-list {
  margin-bottom: 20px;
}
.message-input {
  margin-bottom: 20px;
}
</style>