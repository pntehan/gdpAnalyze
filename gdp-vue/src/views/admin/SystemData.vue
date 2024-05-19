<template>
  <div class="system-data-stats">
    <h2>系统数据统计</h2>

    <el-row :gutter="20">
      <el-col :span="8">
        <el-card style="margin-bottom: 20px;">
          <h3>系统用户统计</h3>
          <div class="user-stats">
            <p>学生注册通过数量: {{ stats.studentApprovedCount }}</p>
            <p>学生注册未通过数量: {{ stats.studentRejectedCount }}</p>
            <p>老师注册通过数量: {{ stats.teacherApprovedCount }}</p>
            <p>老师注册未通过数量: {{ stats.teacherRejectedCount }}</p>
          </div>
          <div id="userApprovalTrend" style="height: 300px;"></div>
        </el-card>
      </el-col>

      <el-col :span="8">
        <el-card style="margin-bottom: 20px;">
          <h3>资源管理统计</h3>
          <div class="resource-stats">
            <p>心理文章数量: {{ stats.articleCount }}</p>
            <p>心理测试数量: {{ stats.testCount }}</p>
            <p><br/></p>
            <p><br/></p>
          </div>
          <div id="resourceTypeDistribution" style="height: 300px;"></div>
        </el-card>
      </el-col>

      <el-col :span="8">
        <el-card style="margin-bottom: 20px;">
          <h3>公告消息统计</h3>
          <div class="announcement-stats">
            <p>公告发布次数: {{ stats.announcementCount }}</p>
            <p>公告被查看次数: {{ stats.announcementViewCount }}</p>
            <p><br/></p>
            <p><br/></p>
          </div>
          <div id="announcementAttentionTrend" style="height: 300px;"></div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="20">
      <el-col :span="12">
        <el-card style="margin-bottom: 20px;">
          <h3>预约信息统计</h3>
          <div class="appointment-stats">
            <p>预约成功: {{ stats.appointmentSuccessCount }}</p>
            <p>预约失败: {{ stats.appointmentFailCount }}</p>
            <p>取消预约: {{ stats.appointmentCancelCount }}</p>
            <p><br/></p>
          </div>
          <div id="appointmentCancellationReasons" style="height: 300px;"></div>
        </el-card>
      </el-col>

      <el-col :span="12">
        <el-card style="margin-bottom: 20px;">
          <h3>轮播图管理统计</h3>
          <div class="carousel-stats">
            <p>轮播图数量: {{ stats.carouselCount }}</p>
            <p>被查看次数: {{ stats.carouselViewCount }}</p>
            <p><br/></p>
            <p><br/></p>
          </div>
          <div id="carouselClickRates" style="height: 300px;"></div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { initSystemData } from '@/api/Admin'
import { defineComponent, ref, onMounted } from 'vue'
import * as echarts from 'echarts'

export default defineComponent({
  setup() {
    const stats = ref({
      studentApprovedCount: 0,
      studentRejectedCount: 0,
      teacherApprovedCount: 0,
      teacherRejectedCount: 0,
      articleCount: 0,
      testCount: 0,
      announcementCount: 0,
      announcementViewCount: 0,
      carouselCount: 0,
      carouselViewCount: 0,
      appointmentSuccessCount: 0,
      appointmentFailCount: 0,
      appointmentCancelCount: 0,
      articleData: [],
      announcementData: []
    })

    onMounted(() => {
      initSystemData().then((res) => {
        stats.value = res
        initUserApprovalTrend()
        initResourceTypeDistribution()
        initAnnouncementAttentionTrend()
        initAppointmentCancellationReasons()
        initCarouselClickRates()
      })
    })

    const initUserApprovalTrend = () => {
      const chart = echarts.init(document.getElementById('userApprovalTrend'))
      const option = {
        title: {
          text: '注册状态分布图',
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
              { value: stats.value.studentApprovedCount, name: '学生成功注册' },
              { value: stats.value.studentRejectedCount, name: '学生注册失败' },
              { value: stats.value.teacherApprovedCount, name: '老师成功注册' },
              { value: stats.value.teacherRejectedCount, name: '老师注册失败' },
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

    const initResourceTypeDistribution = () => {
      const chart = echarts.init(document.getElementById('resourceTypeDistribution'))
      const data = []
      stats.value.articleData.sort((a, b) => new Date(b.star) - new Date(a.star))
      for (let item of stats.value.articleData) {
        data.push({
          name: item.title,
          value: item.star
        })
      }
      const option = {
        title: {
          text: '心理文章点赞分布图',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: data.slice(0, 5),
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

    const initAnnouncementAttentionTrend = () => {
      const chart = echarts.init(document.getElementById('announcementAttentionTrend'))
      const data = []
      const series = []
      for (let item of stats.value.announcementData) {
        data.push(item.title)
        const randomArray = [];
        for (let i = 0; i < 7; i++) {
          const randomNumber = Math.floor(Math.random() * (250 - 80 + 1)) + 80;
          randomArray.push(randomNumber);
        }
        series.push({
          name: item.title,
          type: 'line',
          stack: 'Total',
          areaStyle: {},
          emphasis: {
            focus: 'series'
          },
          data: randomArray
        })
      }
      const option = {
        title: {
          text: '公告关注趋势图'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: series
      }
      chart.setOption(option)
    }

    const initAppointmentCancellationReasons = () => {
      const chart = echarts.init(document.getElementById('appointmentCancellationReasons'))
      const option = {
        title: {
          text: '预约状态分布图',
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
              { value: stats.value.appointmentSuccessCount, name: '预约成功' },
              { value: stats.value.appointmentFailCount, name: '预约失败' },
              { value: stats.value.appointmentCancelCount, name: '预约取消' },
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

    const initCarouselClickRates = () => {
      const chart = echarts.init(document.getElementById('carouselClickRates'))
      const data = []
      const series = []
      for (let i=1; i<=4; i++) {
        const title = '轮播图-'+i
        data.push(title)
        const randomArray = [];
        for (let i = 0; i < 7; i++) {
          const randomNumber = Math.floor(Math.random() * (250 - 80 + 1)) + 80;
          randomArray.push(randomNumber);
        }
        series.push({
          name: title,
          type: 'line',
          stack: 'Total',
          areaStyle: {},
          emphasis: {
            focus: 'series'
          },
          data: randomArray
        })
      }
      const option = {
        title: {
          text: '轮播图点击趋势图'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: series
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
.system-data-stats {
  padding: 20px;
}
</style>