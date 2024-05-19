<template>
  <div class="message-container">
    <el-card class="message-card">
      <template #header>
        <div class="card-header">
          <span>我的消息</span>
        </div>
      </template>
      <el-tabs v-model="activeTab">
        <el-tab-pane label="收件箱" name="inbox">
          <el-table :data="inboxMessages" style="width: 100%">
            <el-table-column label="消息内容" prop="content"></el-table-column>
            <el-table-column label="发送时间" prop="up_time" width="180"></el-table-column>
            <el-table-column label="操作" width="120">
              <template #default="scope">
                <el-button type="text" size="small" @click="markRead(scope.row)">标记已读</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-tab-pane>
        <el-tab-pane label="已读消息" name="read">
          <el-table :data="readMessages" style="width: 100%">
            <el-table-column label="消息内容" prop="content"></el-table-column>
            <el-table-column label="发送时间" prop="up_time" width="180"></el-table-column>
            <el-table-column label="状态" width="120">
              <el-tag type="primary">已读</el-tag>
            </el-table-column>
          </el-table>
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
</template>

<script>
import { getAllMessages, updateMsgStatus } from '@/api/Student'

export default {
  data() {
    return {
      activeTab: 'inbox',
      inboxMessages: [
        // 未读消息数据
      ],
      readMessages: [
        // 已读消息数据
      ]
    }
  },

  mounted() {
    let user_info = JSON.parse(localStorage.getItem('user_info'))
    getAllMessages({student_id: user_info.id}).then((res) => {
      this.inboxMessages = res.inboxMessages
      this.readMessages = res.readMessages
    })
  },

  methods: {
    markRead(message) {
      // 将单条消息标记为已读
      updateMsgStatus({msg_id: message.id}).then((res) => {
        if (res.status == 200) {
          let user_info = JSON.parse(localStorage.getItem('user_info'))
          getAllMessages({student_id: user_info.id}).then((res) => {
            this.inboxMessages = res.inboxMessages
            this.readMessages = res.readMessages
          })
        }
      })
    }
  }
}
</script>

<style scoped>
.message-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.message-card {
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>