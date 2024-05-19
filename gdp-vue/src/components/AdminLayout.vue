<template>
  <div class="admin-layout">
    <admin-header />
    <div class="main-container">
      <admin-sidebar />
      <div class="content">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import AdminHeader from './AdminHeader.vue'
import AdminSidebar from './AdminSidebar.vue'

export default {
  components: {
    AdminHeader,
    AdminSidebar
  }
}
</script>

<style scoped>
.admin-layout {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-container {
  flex: 1;
  display: flex;
}

.content {
  flex: 1;
  padding: 20px;
}
</style>
