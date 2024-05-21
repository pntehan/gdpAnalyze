<template>
  <div class="gdp-data-page">
    <div class="content-container">
      <div class="filter-table-container">
        <div class="filter-container" style="margin-bottom: 20px;">
          <!-- 筛选条件选择框 -->
          <el-select v-model="filters.region" placeholder="请选择省份" @change="filterData" style="width: 25%; margin-right: 20px;" clearable>
            <el-option v-for="region in uniqueRegions" :key="region" :label="region" :value="region" />
          </el-select>
          <el-select v-model="filters.year" placeholder="请选择年份" @change="filterData" style="width: 25%; margin-right: 20px;" clearable>
            <el-option v-for="year in uniqueYears" :key="year" :label="year" :value="year" />
          </el-select>
          <el-select v-model="filters.name" placeholder="请选择产业" @change="filterData" style="width: 25%; margin-right: 20px;" clearable>
            <el-option v-for="name in uniqueNames" :key="name" :label="name" :value="name" />
          </el-select>
          <el-button type="primary" @click="addVisible = true" plain round>新增数据</el-button>
        </div>
        <el-table :data="displayedData" style="width: 100%" :header-cell-style="{ background: '#f5f7fa', color: '#606266' }">
          <!-- 表格列定义 -->
          <el-table-column prop="region" label="省份" width="120"/>
          <el-table-column prop="name" label="项目名"/>
          <el-table-column prop="year" label="年份">
            <template  #default="scope">
              {{ scope.row.year }} 年
            </template>
          </el-table-column>
          <el-table-column prop="value" label="金额(单位：亿)">
            <template  #default="scope">
              {{ scope.row.value }} 亿元
            </template>
          </el-table-column>
          <el-table-column prop="operation" label="操作">
            <template  #default="scope">
              <el-button type="primary" size="small" @click="editData(scope.row)" plain round>修改</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="pagination-container">
          <!-- 分页组件 -->
          <el-pagination
            :current-page="currentPage"
            :page-size="pageSize"
            :total="filteredData.length"
            @current-change="handlePageChange"
            layout="prev, pager, next, total, sizes"
            :page-sizes="[10, 20, 50]"
            @size-change="handleSizeChange"
          />
        </div>
      </div>
      <div class="card-container">
        <el-card>
          <img src="@/assets/bg.jpg" alt="图片" class="card-image">
          <div class="card-text">
            <h3>黄河流域省份GDP数据</h3>
            <p>黄河流域是中国重要的经济区域之一,涵盖了多个省份。对黄河流域省份的GDP进行深入分析和研究,具有重要的现实意义和必要性:</p>
            <ol>
              <li>了解区域经济发展水平：通过对黄河流域省份GDP的分析，识别区域内经济发展的差异和不平衡性。</li>
              <li>把握产业结构变迁：分析三大产业占比与GDP的关系，能够揭示黄河流域省份产业结构的演变趋势。</li>
              <li>预测未来发展趋势：基于对历史数据的分析，可以建立模型预测黄河流域省份未来的经济增长速度和发展趋势。</li>
            </ol>
          </div>
        </el-card>
      </div>
    </div>
    <!-- 新增窗口 -->
    <el-dialog title="新增数据" v-model="addVisible">
      <el-form :model="form" label-width="80px">
        <el-form-item label="省份">
          <el-select v-model="addForm.region" placeholder="请选择省份">
            <el-option
              v-for="province in uniqueRegions"
              :key="province"
              :label="province"
              :value="province">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="产业">
          <el-select v-model="addForm.name" placeholder="请选择产业">
            <el-option
              v-for="name in uniqueNames"
              :key="name"
              :label="name"
              :value="name">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="年份">
          <el-select v-model="addForm.year" placeholder="请选择年份">
            <el-option
              v-for="year in historyYears"
              :key="year"
              :label="year+'年'"
              :value="year">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="金额(亿元)">
          <el-input-number v-model="addForm.value" :precision="2" :step="0.01"></el-input-number>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="addVisible = false">取消</el-button>
        <el-button type="primary" @click="addData">确定</el-button>
      </template>
    </el-dialog>
    <!-- 修改窗口 -->
    <el-dialog title="修改数据" v-model="editVisible">
      <el-form :model="form" label-width="80px">
        <el-form-item label="省份">
          <el-select v-model="editForm.region" placeholder="请选择省份">
            <el-option
              v-for="province in uniqueRegions"
              :key="province"
              :label="province"
              :value="province">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="产业">
          <el-select v-model="editForm.name" placeholder="请选择产业">
            <el-option
              v-for="name in uniqueNames"
              :key="name"
              :label="name"
              :value="name">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="年份">
          <el-select v-model="editForm.year" placeholder="请选择年份">
            <el-option
              v-for="year in uniqueYears"
              :key="year"
              :label="year+'年'"
              :value="year">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="金额(亿元)">
          <el-input-number v-model="editForm.value" :precision="2" :step="0.01"></el-input-number>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="editVisible = false">取消</el-button>
        <el-button type="primary" @click="onEditData">确定</el-button>
      </template>
    </el-dialog>
  </div>
</template>


<script setup>
import { ref, onMounted, defineEmits } from 'vue'
import { getGDPData, editGDPData, addGDPData } from '@/api/Data'
import { ElMessage } from 'element-plus'

const emit = defineEmits(['change-value'])
emit('change-value', 'dataAnalyse')
const gdpData = ref([])
const currentPage = ref(1)
const pageSize = ref(10)
const filters = ref({
  region: '',
  year: '',
  name: ''
})
const uniqueRegions = ref([])
const historyYears = ref([])
const uniqueYears = ref([])
const uniqueNames = ref([])
const filteredData = ref([])
const displayedData = ref([])
const addVisible = ref(false)
const addForm = ref({
  name: '', region: '', year: '', value: ''
})
const editVisible = ref(false)
const editForm = ref({
  id: '', name: '', region: '', year: '', value: ''
})

onMounted(() => {
  getGDPData().then(res => {
    gdpData.value = res
    // 初始化滤波数据
    uniqueRegions.value = [...new Set(gdpData.value.map((item) => item.region))]
    uniqueYears.value = [...new Set(gdpData.value.map((item) => item.year))]
    uniqueNames.value = [...new Set(gdpData.value.map((item) => item.name))]
    historyYears.value = Array.from({ length: 2024 - 1990 + 1 }, (_, i) => 1990 + i)
    // 初始化表格数据
    filteredData.value = gdpData.value
    updateDisplayedData()
  })
})

function filterData() {
  filteredData.value = gdpData.value.filter((item) => {
    // 检查省份筛选条件
    if (filters.value.region && item.region !== filters.value.region) {
      return false
    }
    // 检查年份筛选条件
    if (filters.value.year && item.year !== filters.value.year) {
      return false
    }
    // 检查名称筛选条件
    if (filters.value.name && !item.name.includes(filters.value.name)) {
      return false
    }
    return true
  })
  currentPage.value = 1
  updateDisplayedData()
}

function updateDisplayedData() {
  let startIndex = (currentPage.value - 1) * pageSize.value;
  let endIndex = startIndex + pageSize.value;
  if (endIndex > filteredData.value.length) {
    endIndex = filteredData.value.length;
  }
  displayedData.value = filteredData.value.slice(startIndex, endIndex);
}

function handlePageChange(newPage) {
  currentPage.value = newPage;
  updateDisplayedData();
}

function handleSizeChange(newSize) {
  pageSize.value = newSize;
  currentPage.value = 1;
  updateDisplayedData();
}

function editData(item) {
  editForm.value = item
  editVisible.value = true
}

function addData() {
  const hasEmptyValue = Object.values(addForm.value).some(value => value === '')
  if (!hasEmptyValue) {
    addGDPData(addForm.value).then(res => {
      if (res.status == 200) {
        gdpData.value.push(res.data)
        addVisible.value = false
        ElMessage.success('新增数据成功!')
      }
      else {
        ElMessage.error(res.msg)
      }
    })
  }
  else {
    ElMessage.error('数据不能为空!')
  }
}

function onEditData() {
  const hasEmptyValue = Object.values(editForm.value).some(value => value === '')
  if (!hasEmptyValue) {
    editGDPData(editForm.value).then(res => {
      gdpData.value = gdpData.value.map(item => {
        if (item.id === res.id) {
          return res.data
        }
        return item
      })
      editVisible.value = false
      ElMessage.success('修改数据成功!')
    })
  }
  else {
    ElMessage.error('数据不能为空!')
  }
}
</script>

<style scoped>
.gdp-data-page {
  padding: 50px;
  width: 100%;
}

.content-container {
  display: flex;
}

.filter-table-container {
  flex: 1;
  margin-right: 20px;
}

.pagination-container {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.card-container {
  width: 400px;
  margin-right: 30px;
}

.card-image {
  width: 100%;
  height: auto;
  margin-bottom: 10px;
}

.card-text {
  text-align: center;
}
</style>


