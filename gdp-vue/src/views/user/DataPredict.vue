<template>
  <div class="container" style="margin-left: auto; margin-right: auto; max-width: 1200px;">
    <h1 style="margin-top: 100px;">未来GDP预测</h1>
    <el-row :gutter="24" style="margin: 20px;">
      <el-col :span="12">
        <el-select v-model="selectedProvince" @change="changeRegion()" placeholder="选择省份">
          <el-option
            v-for="province in provinces"
            :key="province"
            :label="province"
            :value="province"
          />
        </el-select>
      </el-col>
      <el-col :span="12">
        <el-radio-group v-model="selectedAlgorithm" @change="changeAlgo()">
          <el-radio-button label="svr">SVM</el-radio-button>
          <el-radio-button label="xgb">XGBoost</el-radio-button>
          <el-radio-button label="forest">决策树</el-radio-button>
        </el-radio-group>
      </el-col>
    </el-row>
    <el-row :gutter="24" style="margin: 20px;">
      <el-col :span="12">
        <div ref="historicalChartRef" style="height: 400px" />
      </el-col>
      <el-col :span="12">
        <el-card>
          <div v-if="selectedAlgorithm === 'svm'">{{ svmDescription }}</div>
          <div v-else-if="selectedAlgorithm === 'xgboost'">{{ xgboostDescription }}</div>
          <div v-else-if="selectedAlgorithm === 'decisionTree'">{{ decisionTreeDescription }}</div>
          <div style="text-align: center;">
            <el-button type="primary" @click="onPredict()" style="margin-top: 20px;">预测</el-button>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <el-row :gutter="24" style="margin: 20px;">
      <el-col :span="12">
        <div ref="predictionChartRef" style="height: 400px" />
      </el-col>
      <el-col :span="12">
        <el-table :data="predictionData" style="width: 100%" :header-cell-style="{ background: '#f5f7fa', color: '#606266' }">
          <!-- 预测数值表格列 -->
          <el-table-column prop="region" label="省份" width="120"/>
          <el-table-column prop="name" label="项目名"/>
          <el-table-column prop="value" label="金额(单位：亿)">
            <template  #default="scope">
              {{ scope.row.value.toFixed(1) }} 亿元
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import { onMounted, ref, defineEmits } from 'vue'
import { getGDPData, predict } from '@/api/Data'
import * as echarts from 'echarts'

const emit = defineEmits(['change-value'])
emit('change-value', 'dataPredict')

const gdpData = ref([])
const selectedProvince = ref('')
const provinces = ref([])
const years = ref([])
const names = ref(['地区生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值'])
const selectedAlgorithm = ref('svr')
const svmDescription = ref('SVM 算法介绍')
const xgboostDescription = ref('XGBoost 算法介绍')
const decisionTreeDescription = ref('决策树算法介绍')
const historicalChartRef = ref(null)
const predictionChartRef = ref(null)
const predictionData = ref([])
const predictionNum = ref(0)

onMounted(() => {
  getGDPData().then(res => {
    gdpData.value = res
    // 初始化滤波数据
    provinces.value = [...new Set(gdpData.value.map((item) => item.region))]
    years.value = [...new Set(gdpData.value.map((item) => item.year))].sort((a, b) => a - b)
    years.value.push(years.value[years.value.length-1]+1)
    selectedProvince.value = provinces.value[0]
    initHistoricalChart()
  })
})

function initHistoricalChart() {
  // 初始化历史数据分布图
  const lineChart = echarts.init(historicalChartRef.value)
  // 数据选择
  const data_list = gdpData.value.filter(item => item.region == selectedProvince.value).sort((a, b) => a.year - b.year)
  const series_data = []
  for (let name of names.value) {
    let data = []
    for (let year of years.value) {
      let d = data_list.find(item => item.year == year && item.name == name)
      if (d) {
        data.push(d.value)
      }
    }
    series_data.push({
      name: name,
      type: 'line',
      data: data
    })
  }
  const option = {
    title: {
      text: selectedProvince.value + '历史数据变化',
      x: 'center',
      y: 'top'
    },
    tooltip: {
      trigger: 'axis'
    },
    legend: {
      data: names.value,
      y: 'bottom',
      padding: [20, 0, 0, 0]
    },
    grid: {
      left: '3%',
      right: '5%',
      bottom: '5%',
      containLabel: true
    },
    toolbox: {
      feature: {
        saveAsImage: {}
      }
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: years.value.sort((a, b) => a - b),
      name: '年份'
    },
    yAxis: {
      type: 'value',
      name: '单位:亿元'
    },
    series: series_data
  }
  // 配置折线图选项
  lineChart.setOption(option)
}

function initPredictionChart() {
  // 初始化预测结果图表
  const pieChart = echarts.init(predictionChartRef.value)
  // 数据选择
  const data = []
  names.value.forEach((name) => {
    if (name == '地区生产总值') { 
      return 
    }
    let item = predictionData.value.find(item => item.name == name)
    data.push(item)
  })
  const option = {
    title: {
      text: selectedProvince.value + years.value[years.value.length-1] + '年三产占比分析',
      x: 'center',
      y: 'top'
    },
    tooltip: {
      trigger: 'item'
    },
    legend: {
      y: 'bottom',
      padding: [20, 0, 0, 0]
    },
    series: [
      {
        name: '单位:亿元',
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
  // 配置饼图选项
  pieChart.setOption(option)
}

function onPredict() {
  // 进行预测
  predict({region: selectedProvince.value, algo: selectedAlgorithm.value, num: predictionNum.value }).then(res => {
    predictionData.value = res
    initPredictionChart()
    // 追加
    for (let item of res) {
      item.year = years.value[years.value.length-1]
      gdpData.value.push(item)
    }
    initHistoricalChart()
    predictionNum.value = predictionNum.value + 1
    years.value.push(years.value[years.value.length-1]+1)
  })
}

function changeRegion() {
  predictionNum.value = 0
  getGDPData().then(res => {
    gdpData.value = res
    years.value = [...new Set(gdpData.value.map((item) => item.year))].sort((a, b) => a - b)
    years.value.push(years.value[years.value.length-1]+1)
    initHistoricalChart()
  })
}

function changeAlgo() {
  predictionNum.value = 0
  getGDPData().then(res => {
    gdpData.value = res
    years.value = [...new Set(gdpData.value.map((item) => item.year))].sort((a, b) => a - b)
    years.value.push(years.value[years.value.length-1]+1)
    initHistoricalChart()
  })
}
</script>