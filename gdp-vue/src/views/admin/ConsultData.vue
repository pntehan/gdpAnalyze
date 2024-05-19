<template>
  <div class="business-data-stats">
    <h2>业务数据统计</h2>

    <el-row :gutter="20">
      <el-col :span="12">
        <el-card style="margin-bottom: 20px;">
          <h3>咨询信息统计</h3>
          <div class="consultation-stats">
            <p>总咨询问题数量: {{ stats.totalConsultations }}</p>
            <p><br/></p>
          </div>
          <div id="consultationTopicCloud" style="height: 300px;"></div>
        </el-card>
      </el-col>

      <el-col :span="12">
        <el-card style="margin-bottom: 20px;">
          <h3>心理预警统计</h3>
          <div class="warning-stats">
            <p>总预警次数: {{ stats.warningNum }}</p>
            <p><br/></p>
          </div>
          <div id="warningTrends" style="height: 300px;"></div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="20">
      <el-col :span="12">
        <el-card style="margin-bottom: 20px;">
          <h3>反馈管理统计</h3>
          <div class="feedback-stats">
            <p>总反馈数量: {{ stats.totalFeedbacks }}</p>
            <p><br/></p>
          </div>
          <div id="feedbackHotspots" style="height: 300px;"></div>
        </el-card>
      </el-col>

      <el-col :span="12">
        <el-card style="margin-bottom: 20px;">
          <h3>评价管理统计</h3>
          <div class="review-stats">
            <p>总评价数量: {{ stats.totalReviews }}</p>
            <p>平均评分: {{ stats.averageRating }}</p>
          </div>
          <div id="teacherRatingDistribution" style="height: 300px;"></div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { initConsultData } from '@/api/Admin'
import { defineComponent, ref, onMounted } from 'vue'
import * as echarts from 'echarts'
import 'echarts-wordcloud'

export default defineComponent({
  setup() {
    const stats = ref({
      averageRating: 0,
      consultReplyNum: 0,
      feedbackReplyNum: 0,
      status: 0,
      totalConsultations: 0,
      totalFeedbacks: 0,
      totalRecords: 0,
      totalReviews: 0,
      warningNum: 0,
      wordFrequency1: [],
      wordFrequency2: [],
      scoreData: []
    })

    onMounted(() => {
      // 取值
      initConsultData().then((res) => {
        stats.value = res
        // 画图
        initConsultationTopicCloud()
        initWarningTrends()
        initFeedbackHotspots()
        initTeacherRatingDistribution()
      })
    })

    const getRandomColor = () => {
      const letters = '0123456789ABCDEF'
      let color = '#'
      for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)]
      }
      return color
    }

    const initConsultationTopicCloud = () => {
      const chart = echarts.init(document.getElementById('consultationTopicCloud'))
      const data = [] 
      for (let word in stats.value.wordFrequency1) {
        data.push({
          name: word,
          value: stats.value.wordFrequency1[word],
          textStyle: {
            fontFamily: 'sans-serif',
            fontWeight: 'bold',
            color: getRandomColor()
          }
        })
      }
      const option = {
        title: {
          text: '咨询内容词云图',
          left: 'center'
        },
        series: [
          {
            type: 'wordCloud',
            gridSize: 2,
            sizeRange: [12, 50],
            rotationRange: [-90, 90],
            shape: 'circle',
            left: 'center',
            top: 'center',
            width: '70%',
            height: '80%',
            drawOutOfBound: true,
            keepAspect: false,
            data: data
          }
        ]
      }
      chart.setOption(option)
    }

    const initWarningTrends = () => {
      const chart = echarts.init(document.getElementById('warningTrends'))
      const option = {
        title: {
          text: '预警信息分布图',
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
              { value: stats.value.warningNum, name: '进行预警' },
              { value: stats.value.totalRecords-stats.value.warningNum, name: '不进行预警' },
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

    const initFeedbackHotspots = () => {
      const chart = echarts.init(document.getElementById('feedbackHotspots'))
      const data = [] 
      for (let word in stats.value.wordFrequency2) {
        data.push({
          name: word,
          value: stats.value.wordFrequency2[word],
          textStyle: {
            fontFamily: 'sans-serif',
            fontWeight: 'bold',
            color: getRandomColor()
          }
        })
      }
      const option = {
        title: {
          text: '反馈问题词云图',
          left: 'center'
        },
        series: [
          {
            type: 'wordCloud',
            gridSize: 2,
            sizeRange: [12, 50],
            rotationRange: [-90, 90],
            shape: 'circle',
            left: 'center',
            top: 'center',
            width: '70%',
            height: '80%',
            drawOutOfBound: true,
            keepAspect: false,
            data: data
          }
        ]
      }
      chart.setOption(option)
    }

    const initTeacherRatingDistribution = () => {
      const chart = echarts.init(document.getElementById('teacherRatingDistribution'))
      const data = []
      for (let item in stats.value.scoreData) {
        data.push({
          name: item + '分',
          value: stats.value.scoreData[item]
        })
      }
      const option = {
        title: {
          text: '评价分值分布图',
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
            data: data,
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
      stats,
      getRandomColor
    }
  }
})
</script>

<style scoped>
.business-data-stats {
  padding: 20px;
}
</style>