<template>
  <div class="user-data-stats">
    <h2>用户数据统计</h2>

    <el-row :gutter="20">
      <el-col :span="8">
        <el-card>
          <h3>用户统计</h3>
          <div class="user-stats">
            <p>注册学生总数: {{ stats.totalStudents }}</p>
            <p>注册老师总数: {{ stats.totalTeachers }}</p>
            <p>管理员总数: {{ stats.totalAdmins }}</p>
          </div>
          <div id="genderRatioChart" style="height: 300px;"></div>
        </el-card>
      </el-col>

      <el-col :span="8">
        <el-card>
          <h3>心理测试统计</h3>
          <div class="test-stats">
            <p>总提交数量: {{ stats.totalRecords }}</p>
            <p>总通过数量: {{ stats.passRecords }}</p>
            <p><br/></p>
          </div>
          <div id="testScoreDistribution" style="height: 300px;"></div>
        </el-card>
      </el-col>

      <el-col :span="8">
        <el-card>
          <h3>预约统计</h3>
          <div class="appointment-stats">
            <p>总预约次数: {{ stats.totalAppointments }}</p>
            <p>最高预约老师: {{ stats.topAppointedTeacher }}</p>
            <p><br/></p>
          </div>
          <div id="appointmentTrends" style="height: 300px;"></div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { initUserData } from '@/api/Admin'
import { defineComponent, ref, onMounted } from 'vue'
import * as echarts from 'echarts'

export default defineComponent({
  setup() {
    const stats = ref({
      totalStudents: 1000,
      totalTeachers: 50,
      totalAdmins: 5,
      totalRecords: 2000,
      passRecords: 1500,
      totalAppointments: 3000,
      appointmentData: '',
      topAppointedTeacher: ''
    })

    onMounted(() => {
      initUserData().then((res) => {
        stats.value.totalStudents = res.totalStudents
        stats.value.totalTeachers = res.totalTeachers
        stats.value.totalAdmins = res.totalAdmins
        stats.value.totalRecords = res.totalRecords
        stats.value.passRecords = res.passRecords
        stats.value.totalAppointments = res.totalAppointments
        stats.value.appointmentData = res.appointmentData
        initGenderRatioChart()
        initTestScoreDistribution()
        initAppointmentTrends()
      })
    })

    const initGenderRatioChart = () => {
      const chart = echarts.init(document.getElementById('genderRatioChart'))
      const option = {
        title: {
          text: '注册用户分布图',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: [
              { value: stats.value.totalStudents, name: '学生' },
              { value: stats.value.totalTeachers, name: '老师' },
              { value: stats.value.totalAdmins, name: '管理员' },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      }
      chart.setOption(option)
    }

    const initTestScoreDistribution = () => {
      const chart = echarts.init(document.getElementById('testScoreDistribution'))
      const option = {
        title: {
          text: '测试情况分布图',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: [
              { value: stats.value.passRecords, name: '通过测试' },
              { value: stats.value.totalRecords-stats.value.passRecords, name: '未通过测试' }
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      }
      chart.setOption(option)
    }

    const initAppointmentTrends = () => {
      const chart = echarts.init(document.getElementById('appointmentTrends'))
      // 预约数据处理
      const num_info = {}
      stats.value.appointmentData.forEach((item) => {
        const name = item.teacher_name
        num_info[name] = (num_info[name] || 0) + 1
      })
      const data = stats.value.appointmentData
      stats.value.topAppointedTeacher = data[0].name
      const option = {
        title: {
          text: '测试情况分布图',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: data.slice(0, 10),
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      }
      chart.setOption(option)
    }

    return {
      stats
    }
  }
})
</script>

<style scoped>
.user-data-stats {
  padding: 20px;
}

.user-stats,
.test-stats,
.appointment-stats {
  margin-bottom: 20px;
}
</style>