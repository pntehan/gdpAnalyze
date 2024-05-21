<template>
  <el-container class="main-container" style="margin-left: auto; margin-right: auto; max-width: 1200px;">
    <el-row :gutter="24">
      <el-col :span="6" style="margin-top: 20px; margin-bottom: 20px;">
        <el-card>
          <el-form>
            <el-form-item label="省份">
              <el-select v-model="selectedProvince" @change="changeRegion()" placeholder="选择省份">
                <el-option
                  v-for="province in provinces"
                  :key="province"
                  :label="province"
                  :value="province"
                />
              </el-select>
            </el-form-item>
            <el-form-item label="年份">
              <el-select v-model="selectedYear" @change="changeYear()" placeholder="选择年份">
                <el-option
                  v-for="year in years"
                  :key="year"
                  :label="year"
                  :value="year"
                />
              </el-select>
            </el-form-item>
          </el-form>
          <el-table :data="tableData" max-height="300">
            <el-table-column prop="name" label="指标名称" />
            <el-table-column prop="value" label="金额(亿元)" />
          </el-table>
        </el-card>
      </el-col>
      <el-col :span="18" style="margin-top: 20px; margin-bottom: 20px">
        <el-card>
          <div ref="lineChartRef" style="height: 400px" />
        </el-card>
      </el-col>
    </el-row>
    <el-footer>
      <el-row :gutter="24">
        <el-col :span="12" style="margin-bottom: 20px;">
          <el-card>
            <div ref="pieChartRef" style="height: 400px" />
          </el-card>
        </el-col>
        <el-col :span="12" style="margin-bottom: 20px;">
          <el-card>
            <div ref="barChartRef" style="height: 400px" />
          </el-card>
        </el-col>
        <el-col :span="12" style="margin-bottom: 100px;">
          <el-card>
            <div ref="radarChartRef" style="height: 400px" />
          </el-card>
        </el-col>
        <el-col :span="12" style="margin-bottom: 100px;">
          <el-card>
            <div ref="diskChartRef" style="height: 400px" />
          </el-card>
        </el-col>
      </el-row>
    </el-footer>
  </el-container>
</template>

<script setup>
import { ref, onMounted, watchEffect, defineEmits } from 'vue'
import * as echarts from 'echarts'
import { getGDPData } from '@/api/Data'

const emit = defineEmits(['change-value'])
emit('change-value', 'dataShow')
const gdpData = ref([])
const selectedProvince = ref('')
const selectedYear = ref('')
const provinces = ref([])
const years = ref([])
const names = ref(['地区生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值'])
const tableData = ref([])

const lineChartRef = ref(null)
const pieChartRef = ref(null)
const barChartRef = ref(null)
const radarChartRef = ref(null)
const diskChartRef = ref(null)

onMounted(() => {
  // 从服务端获取省份和年份数据、
  getGDPData().then(res => {
    gdpData.value = res
    // 初始化滤波数据
    provinces.value = [...new Set(gdpData.value.map((item) => item.region))]
    years.value = [...new Set(gdpData.value.map((item) => item.year))].sort((a, b) => a - b)
    // names.value = [...new Set(gdpData.value.map((item) => item.name))]
    selectedProvince.value = provinces.value[0]
    selectedYear.value = years.value[0]
    // 初始化表格数据
    tableData.value = fetchTableData(selectedProvince.value, selectedYear.value)
    // 初始化图表
    initLineChart()
    initPieChart()
    initBarChart()
    initRadarChart()
    initDiskChart()
  })
})

watchEffect(() => {
  // 当省份或年份改变时,更新表格数据
  tableData.value = fetchTableData(selectedProvince.value, selectedYear.value)
})


function fetchTableData(province, year) {
  // 从服务端获取表格数据
  return gdpData.value.filter(item => item.region == province && item.year == year)
}

function changeRegion() {
  initLineChart()
  initPieChart()
  initRadarChart()
}

function changeYear() {
  initBarChart()
  initPieChart()
  initRadarChart()
}

function initLineChart() {
  const lineChart = echarts.init(lineChartRef.value)
  // 数据选择
  const data_list = gdpData.value.filter(item => item.region == selectedProvince.value).sort((a, b) => a.year - b.year)
  const series_data = []
  for (let name of names.value) {
    let data = []
    for (let year of years.value) {
      let d = data_list.find(item => item.year == year && item.name == name)
      data.push(d.value)
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

function initPieChart() {
  const pieChart = echarts.init(pieChartRef.value)
  // 数据选择
  const data = []
  names.value.forEach((name) => {
    if (name == '地区生产总值') { 
      return 
    }
    let item = tableData.value.find(item => item.name == name)
    data.push(item)
  })
  const option = {
    title: {
      text: selectedProvince.value + selectedYear.value + '年三产占比分析',
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

function initBarChart() {
  const barChart = echarts.init(barChartRef.value)
  // 数据选择
  const data_list = gdpData.value.filter(item => item.year == selectedYear.value)
  const data_sort = data_list.filter(item => item.name == '地区生产总值').sort((a, b) => a.value - b.value)
  const provinces_sort = []
  data_sort.forEach((item) => { 
    provinces_sort.push(item.region)
  })
  // 数据处理
  const series_data = []
  for (let name of names.value) {
    let ds = data_list.filter(item => item.name == name).sort((a, b) => a.value - b.value)
    let data = []
    for (let d of ds) {
      data.push(d.value)
    }
    series_data.push({
      name: name, 
      type: 'bar',
      data: data
    })
  }
  const option = {
    title: {
      text: selectedYear.value+'年黄河流域省份GDP排名',
      x: 'center',
      y: 'top'
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    legend: {
      y: 'bottom',
      padding: [20, 0, 0, 0]
    },
    grid: {
      left: '3%',
      right: '13%',
      bottom: '6%',
      containLabel: true
    },
    xAxis: {
      type: 'value',
      boundaryGap: [0, 0.01],
      name: '单位:亿元'
    },
    yAxis: {
      type: 'category',
      data: provinces_sort
    },
    series: series_data
  }
  // 配置柱状图选项
  barChart.setOption(option)
}

function initRadarChart() {
  const radarChart = echarts.init(radarChartRef.value)
  // 数据准备
  const series_data = []
  const indicator = []
  let max_data = 0
  for (let data of tableData.value) {
    if (data.name == '地区生产总值') {
      continue
    }
    series_data.push(data.value)
    if (data.value > max_data) {
      max_data = data.value
    }
  }
  for (let data of tableData.value) {
    if (data.name == '地区生产总值') {
      continue
    }
    indicator.push({
      name: data.name,
      max: max_data
    })
  }
  const option = {
    title: {
      text: selectedProvince.value+selectedYear.value+'子产业产值对比图',
      x: 'center',
      y: 'top'
    },
    grid: {
      top: '10%',
      left: '5%',
      right: '5%',
      bottom: '0%',
      containLabel: true
    },
    radar: {
      // shape: 'circle',
      indicator: indicator
    },
    series: [
      {
        name: '产业数据分布',
        type: 'radar',
        data: [
          {
            value: series_data,
            name: selectedProvince.value
          }
        ]
      }
    ]
}
  // 配置散点图选项
  radarChart.setOption(option)
}

function initDiskChart() {
  const diskChart = echarts.init(diskChartRef.value)
  // 数据处理
  const diskData = []
  for (let province of provinces.value) {
    let item = {
      'value': 0,
      'name': province,
      'path': province,
      'children': []
    }
    for (let year of years.value) {
      let item_i = {
        'value': 0,
        'name': province+'/'+year,
        'path': province+'/'+year,
        'children': []
      }
      for (let name of names.value) {
        let item_j = {
          'value': gdpData.value.find(item => item.region == province && item.year == year && item.name == name).value,
          'name': province+'/'+year+'.'+name,
          'path': province+'/'+year+'.'+name
        }
        item_i.value = item.value + item_j.value
        item_i.children.push(item_j)
      }
      item.value = item.value + item_i.value
      item.children.push(item_i)
    }
    diskData.push(item)
  }
  const option = {
    title: {
      text: '黄河流域全部数据展示',
      left: 'center'
    },
    tooltip: {
      formatter: function (info) {
        let name = info.name
        let value = info.value;
        let treePathInfo = info.treePathInfo;
        let treePath = []
        for (let i = 1; i < treePathInfo.length; i++) {
          treePath.push(treePathInfo[i].name)
        }
        return [
          '<div class="tooltip-title">' +
            name +
            '</div>',
          '金额: ' + value + ' 亿元'
        ].join('');
      }
    },
    series: [
      {
        name: 'gdp数据',
        type: 'treemap',
        visibleMin: 300,
        label: {
          show: true,
          formatter: '{b}'
        },
        itemStyle: {
          borderColor: '#fff'
        },
        levels: getLevelOption(),
        data: diskData
      }
    ]
  }
  // 配置磁盘图选项
  diskChart.setOption(option)
}

function getLevelOption() {
  return [
    {
      itemStyle: {
        borderWidth: 0,
        gapWidth: 5
      }
    },
    {
      itemStyle: {
        gapWidth: 1
      }
    },
    {
      colorSaturation: [0.35, 0.5],
      itemStyle: {
        gapWidth: 1,
        borderColorSaturation: 0.6
      }
    }
  ]
}
</script>
