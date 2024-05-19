<template>
  <div class="admin-sidebar">
    <el-menu
      :default-active="activeIndex"
      class="el-menu-vertical-demo"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      router
    >
      <el-menu-item index="/admin">
        <el-icon><icon-menu /></el-icon>
        <span>后台首页</span>
      </el-menu-item>
      <el-menu-item index="/admin/userData">
        <el-icon><document /></el-icon>
        <span>用户数据统计</span>
      </el-menu-item>
      <el-menu-item index="/admin/consultData">
        <el-icon><setting /></el-icon>
        <span>心理数据统计</span>
      </el-menu-item>
      <el-menu-item index="/admin/systemData">
        <el-icon><ChatLineSquare /></el-icon>
        <span>系统数据统计</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import { Document, Menu as IconMenu, Setting, ChatLineSquare } from '@element-plus/icons-vue'
import { computed } from 'vue'
import { useRoute } from 'vue-router'

export default {
  components: {
    Document,
    IconMenu,
    Setting,
    ChatLineSquare
  },

  setup() {
    const route = useRoute()
    const activeIndex = computed(() => {
      const menuIndex = route.meta.menuIndex
      return menuIndex || ''
    })

    return {
      activeIndex
    }
  }
}
</script>

<style scoped>
.admin-sidebar {
  width: 200px;
  background-color: #545c64;
}
</style>