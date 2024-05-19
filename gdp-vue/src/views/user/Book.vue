<template>
  <div class="appointment-center">
    <div class="main-content">
      <div class="search-bar">
        <el-input v-model="searchText" placeholder="搜索老师" prefix-icon="el-icon-search"></el-input>
      </div>
      <div class="teacher-list">
        <el-row :gutter="20">
          <el-col :span="8" v-for="(teacher, index) in filteredTeachers" :key="index">
            <el-card :body-style="{ padding: '0px' }" shadow="hover" style="margin-bottom: 20px;">
              <img :src="teacher.avatar" class="teacher-avatar" />
              <div class="teacher-info">
                <h3 class="teacher-name">{{ teacher.name }}</h3>
                <p class="teacher-intro">{{ teacher.intro }}</p>
                <div class="appointment-button">
                  <el-button :icon="Star" @click="starTeacher(teacher.id)" circle />
                  <el-button type="primary" @click="makeAppointment(teacher)">预约</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <div style="display: flex; justify-content: center;" v-if="not_search">
          <el-pagination
            :current-page="currentPage"
            :page-size="pageSize"
            :total="totalItems"
            layout="prev, pager, next"
            @current-change="handleCurrentChange"
          ></el-pagination>
        </div>
      </div>
    </div>
    <div class="sidebar">
      <h3>当前预约</h3>
      <ul class="appointment-list">
        <li v-if="appointments.length==0">
          <span>还没有预约</span>
        </li>
        <li v-for="(appointment, index) in appointments" :key="index">
          <span>{{ appointment.teacher_name }}</span>
          <span>{{ appointment.up_time }}</span>
          <el-button type="text" @click="cancelAppointment(index)">取消</el-button>
        </li>
      </ul>
      <h3>预约记录</h3>
      <el-table :data="tableData" style="width: 100%" max-height="600">
        <el-table-column prop="up_time" label="时间" width="120" />
        <el-table-column prop="teacher_name" label="预约老师" show-overflow-tooltip />
        <el-table-column prop="status" label="预约情况" show-overflow-tooltip />
        <el-table-column label="操作" width="100">
          <template #default="scope">
            <el-button type="text" @click="openComment(scope.row)" :disabled="scope.row.status!='成功预约'">评价</el-button>
            <el-button type="text" @click="lookComment(scope.row)" :disabled="scope.row.status!='成功预约'">查看</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <el-dialog v-model="commentDialogVisible" title="评价内容">
      <el-input label="评价" v-model="comment.content" style="margin-top: 20px;">
        <template #prepend>评价</template>
      </el-input>
      <div style="display: flex; justify-content: center;">
        <el-rate v-model="comment.star" :colors="colors" allow-half/>
      </div>
      <div style="display: flex; justify-content: center;">
        <el-button type="primary" @click="submitComment">提交</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script setup>
import { Star } from '@element-plus/icons-vue'
</script>

<script>
import { getRecords, initBook, getBooks, addBook, cancelBook, addStarTeacher, checkComment, addComment, showComment } from '@/api/Student'
import { ElMessage, ElMessageBox } from 'element-plus'

export default {
  data() {
    return {
      searchText: '',
      all_data: [],
      teachers: [],
      appointments: [],
      maxAppointmentsPerDay: 2,
      currentPage: 1,
      pageSize: 3,
      totalItems: 1,
      not_search: true,
      // 记录表格
      tableData: [],
      commentDialogVisible: false,
      comment: {
        appointment_id: 0,
        student_id: 0,
        teacher_id: 0,
        content: '',
        star: 0
      },
      colors: ['#99A9BF', '#F7BA2A', '#FF9900']
    }
  },

  mounted() {
    this.$emit('change-value', 'book')
    // 校验
    let user_info = JSON.parse(localStorage.getItem('user_info'))
    getRecords({ student_id: user_info.id }).then((res) => {
      if (res.data.length > 0) {
        ElMessage.success({message: '欢迎预约~', duration: 800})
      }
      else {
        ElMessageBox.alert('您还未进行心理测评，请完成心理测评后，再进行预约!', '系统提示', {
          confirmButtonText: 'OK',
        }).then(() => {
          ElMessage({
            type: 'success',
            message: '自动跳转~',
          })
          this.$router.push('/exam')
        })
        .catch((err) => {
          if (err === 'cancel') {
            // 可以在这里添加一些自定义操作
            console.log('用户手动关闭了 MessageBox');
          }
          ElMessage({
            type: 'success',
            message: '自动跳转~',
          })
          this.$router.push('/exam')
        })
      }
    })
    // 老师信息获取
    initBook().then((res) => {
      for (let i=0; i<res.data.length; i++) {
        this.all_data.push(
          {
            id: res.data[i].id,
            name: res.data[i].name,
            intro: res.data[i].intro,
            avatar: ''
          }
        )
        if (res.data[i].gender == '男') {
          this.all_data[i].avatar = require('@/assets/m_t.jpg')
        }
        else {
          this.all_data[i].avatar = require('@/assets/f_t.jpg')
        }
      }
      this.totalItems = this.all_data.length
      this.handleCurrentChange(1)
    })
    // 历史预约记录获取
    getBooks({ student_id: user_info.id }).then((res) => {
      this.genData(res)
    })
  },

  computed: {
    filteredTeachers() {
      if (this.searchText != '') {
        // eslint-disable-next-line vue/no-side-effects-in-computed-properties
        this.not_search = false
        return this.all_data.filter(teacher => teacher.name.includes(this.searchText))
      }
      // eslint-disable-next-line vue/no-side-effects-in-computed-properties
      this.not_search = true
      return this.teachers
    },
    canAppointment() {
      return this.appointments.length < this.maxAppointmentsPerDay
    }
  },

  methods: {
    handleCurrentChange(index) {
      this,this.currentPage = index
      this.teachers = []
      for (let i=0; i<this.pageSize; i++) {
        let ind = (this.currentPage-1)*this.pageSize + i
        if (ind >= this.totalItems) {
          break
        }
        this.teachers.push(this.all_data[ind])
      }
    },

    makeAppointment(teacher) {
      if (this.canAppointment) {
        let user_info = JSON.parse(localStorage.getItem('user_info'))
        let params = {
          student_id: user_info.id,
          teacher_id: teacher.id,
          status: '等待中'
        }
        addBook(params).then((res) => {
          this.genData(res)
          ElMessage.success('预约申请成功，请耐心等待~')
        })
      } 
      else {
        this.$message.warning('今日预约次数已达上限')
      }
    },

    cancelAppointment(index) {
      cancelBook(this.appointments[index]).then((res) => {
        this.genData(res)
        ElMessage.success('预约取消成功~')
      })
    },

    genData(res) {
      this.tableData = []
      this.appointments = []
      for (let i=0; i<res.data.length; i++) {
        // 将字符串转换为 Date 对象
        let dateTime = new Date(res.data[i].up_time)
        // 获取年月日
        let year = dateTime.getFullYear()
        let month = String(dateTime.getMonth() + 1).padStart(2, '0')
        let day = String(dateTime.getDate()).padStart(2, '0')
        // 获取小时分钟秒
        let hours = String(dateTime.getHours()).padStart(2, '0')
        let minutes = String(dateTime.getMinutes()).padStart(2, '0')
        let seconds = String(dateTime.getSeconds()).padStart(2, '0')
        res.data[i].up_time = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`
        // 根据状态分别添加
        if (res.data[i].status == '等待中') {
          this.appointments.push(res.data[i])
        }
        else {
          this.tableData.push(res.data[i])
        }
      }
      this.tableData.sort((a, b) => new Date(b.up_time) - new Date(a.up_time))
      this.appointments.sort((a, b) => new Date(b.up_time) - new Date(a.up_time))
    },

    starTeacher(teacher_id) {
      let user_info = JSON.parse(localStorage.getItem('user_info'))
      let params = {
        student_id: user_info.id,
        teacher_id: teacher_id
      }
      addStarTeacher(params).then((res) => {
        if (res.status == 200) {
          ElMessage.success('您已成功收藏该老师~')
        }
        else {
          ElMessage.warning('您以及收藏过该老师了哦~')
        }
      })
    },

    openComment(item) {
      if (item.status != '成功预约') {
        ElMessage.error('对于未成功的预约不可评价!')
        return
      }
      // 进行校验
      checkComment({appointment_id: item.id}).then((res) => {
        if (res.status != 200) {
          ElMessage.error('已经评价过啦!')
          return
        }
        else {
          let user_info = JSON.parse(localStorage.getItem('user_info'))
          this.comment.appointment_id = item.id
          this.comment.student_id = user_info.id
          this.comment.teacher_id = item.teacher_id
          this.commentDialogVisible = true
        }
      })
    },

    submitComment() {
      this.comment.star = this.comment.star * 2
      addComment(this.comment).then((res) => {
        if (res.status == 200) {
          this.commentDialogVisible = false
          this.comment = {
            appointment_id: 0,
            student_id: 0,
            teacher_id: 0,
            content: '',
            star: 0
          }
          ElMessage.success('成功评价!')
        }
      })
    },

    lookComment(item) {
      showComment({appointment_id: item.id}).then((res) => {
        if (res.status != 200) {
          ElMessage.error('还没有评价!')
          return
        }
        else {
          ElMessageBox.alert(res.data.content, '评价内容').catch(err => {
            // 捕获点击 X 号关闭按钮的情况
            if (err === 'cancel') {
              // 可以在这里添加一些自定义操作
              console.log('用户手动关闭了 MessageBox');
            }
          })
        }
      })
    }
  }
}
</script>

<style scoped>
.appointment-center {
  display: flex;
  margin-left: 15%;
  margin-right: 15%;
}

.main-content {
  flex: 1;
  padding: 20px;
}

.search-bar {
  margin-bottom: 20px;
}

.teacher-avatar {
  width: 100%;
  height: 400px;
  object-fit: cover;
}

.teacher-info {
  padding: 20px;
}

.teacher-name {
  font-size: 18px;
  margin-bottom: 10px;
}

.teacher-intro {
  color: #666;
  line-height: 1.6;
}

.appointment-button {
  margin-top: 20px;
  text-align: right;
}

.sidebar {
  margin: 20px;
  width: 400px;
  padding: 20px;
  background-color: #f5f5f5;
}

.appointment-list {
  list-style: none;
  padding: 0;
}

.appointment-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}
</style>