<template>
  <div class="profile-page">
    <h2>个人中心</h2>
    <el-form
      :model="userForm"
      :rules="rules"
      ref="userFormRef"
      label-width="120px"
      class="profile-form"
    >
      <el-form-item label="头像">
        <el-avatar shape="square" :size="300" :src="require('@/assets/user.jpg')" />
      </el-form-item>
      <el-form-item label="姓名" prop="name">
        <el-input v-model="userForm.name"></el-input>
      </el-form-item>
      <el-form-item label="学号" prop="id">
        <el-input v-model="userForm.id" disabled></el-input>
      </el-form-item>
      <el-form-item label="班级" prop="classroom">
        <el-input v-model="userForm.classroom" disabled></el-input>
      </el-form-item>
      <el-form-item label="性别" prop="gender">
        <el-radio-group v-model="userForm.gender" class="ml-4">
          <el-radio value="男" size="large">男</el-radio>
          <el-radio value="女" size="large">女</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="自我介绍" prop="intro">
        <el-input v-model="userForm.intro"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input v-model="userForm.password"></el-input>
      </el-form-item>
      <el-form-item label="确认密码" prop="con_password">
        <el-input v-model="userForm.con_password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">保存修改</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { defineComponent, onMounted, ref } from 'vue'
import { ElMessage } from 'element-plus'
import { Plus } from '@element-plus/icons-vue'
import { updateUser } from '@/api/Student.js';

export default defineComponent({
  setup(props, { emit }) {
    const userForm = ref({
      id: '',
      classroom: '',
      name: '',
      gender: '',
      intro: '',
      password: '',
      con_password: ''
    })

    emit('change-value', '')

    onMounted(() => {
      let user_info = JSON.parse(localStorage.getItem('user_info'))
      userForm.value.id = user_info.id
      userForm.value.classroom = user_info.classroom
      userForm.value.name = user_info.name
      userForm.value.gender = user_info.gender
      userForm.value.intro = user_info.intro
      userForm.value.password = user_info.password
      userForm.value.con_password = user_info.password
    })

    const userFormRef = ref(null)

    const rules = {
      id: [
        { required: true, message: '请输入学号', trigger: 'blur' },
      ],
      classroom: [
        { required: true, message: '请输入班级号', trigger: 'blur' },
      ],
      name: [
        { required: true, message: '请输入姓名', trigger: 'blur' },
        { min: 2, max: 6, message: '用户名长度在 2 到 6 个字符', trigger: 'blur' }
      ],
      gender: [
        { required: true, message: '请选择性别', trigger: 'blur' }
      ],
      password: [
        { required: true, message: '请输入密码', trigger: 'blur' }
      ],
      con_password: [
        { required: true, message: '请再次输入密码', trigger: 'blur' }
      ]
    }

    const submitForm = () => {
      userFormRef.value.validate((valid) => {
        if (valid) {
          // 提交表单逻辑
          if (userForm.value.con_password != userForm.value.password) {
            ElMessage.error('两次密码输入不一致!')
            return false
          }
          // 提交
          updateUser(userForm.value).then((res) => {
            localStorage.setItem('user_info', JSON.stringify(res.data))
            userForm.value.id = res.data.id
            userForm.value.classroom = res.data.classroom
            userForm.value.name = res.data.name
            userForm.value.gender = res.data.gender
            userForm.value.intro = res.data.intro
            userForm.value.password = res.data.password
            userForm.value.con_password = res.data.password
            ElMessage.success('修改成功!')
          })
        } else {
          ElMessage.error('请按要求输入信息!')
          return false
        }
      })
    }

    return {
      userForm,
      userFormRef,
      rules,
      submitForm,
      Plus
    }
  }
})
</script>

<style scoped>
.profile-page {
  padding: 20px;
  margin-left: 20%;
  margin-right: 20%;
}
.profile-form {
  max-width: 400px;
}
.avatar-uploader {
  display: flex;
  justify-content: center;
}
.avatar-uploader .avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}
.avatar-uploader .avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 100px;
  height: 100px;
  line-height: 100px;
  text-align: center;
  border: 1px dashed #d9d9d9;
  border-radius: 50%;
}
</style>
