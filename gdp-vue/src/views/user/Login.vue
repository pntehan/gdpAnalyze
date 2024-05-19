<template>
  <div class="login-wrap">
    <div class="login-main">
      <div class="main-panel">
        <div class="panel-left">
          <img src="@/assets/student.jpg" class="left-image" />
        </div>
        <div class="panel-right">
          <div class="panel-head">
            <div class="head-line-left"></div>
            <div class="head-title">大学生心理健康系统 - 学生登陆</div>
            <div class="head-line-right"></div>
          </div>
          <el-form :model="form" :rules="rules" ref="login">
            <el-form-item prop="id">
              <el-input v-model="form.id" placeholder="学号" class="inputLength">
                <el-icon><User /></el-icon>
              </el-input>
            </el-form-item>
            <el-form-item prop="password">
              <el-input
                type="password"
                placeholder="密码"
                v-model="form.password"
                @keyup.enter="submitForm()"
                class="inputLength"
              >
                <el-icon><Key /></el-icon>
              </el-input>
            </el-form-item>
            <div class="tip">Tips : 请输入您的学号与密码。</div>
            <div class="login-btn" @click="submitForm()">登录</div>
            <div class="login-btn" @click="this.$router.push('/s_register')">注册</div>
          </el-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { User, Key } from '@element-plus/icons-vue'
import { login } from '@/api/Student.js'

export default {
  components: {
    User,
    Key
  },

  data: function () {
    return {
      form: {
        id: '',
        password: ''
      }, //登录表单
      rules: {
        id: [
          { required: true, message: '请输入您的学号', trigger: 'blur' },
        ],
        password: [
          { required: true, message: '请输入您的密码', trigger: 'blur' }
        ]
      }
    };
  },

  methods: {
    //登录
    submitForm() {
      let params = {
        id: this.form.id,
        password: this.form.password,
      }
      login(params).then((res) => {
          let { data, status, msg } = res
          localStorage.setItem('user_info', JSON.stringify(data))
          if (status == '200') {
            this.$message.success('登录成功')
            this.$router.push('/home')
          } else {
            this.$message.error('登录失败:' + msg)
          }
      })
      .catch((error) => {
        this.$message.error('登录失败!' + error)
      })
    },
  }
};
</script>

<style scoped lang="less">
.login-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  background: #fff;
}

.login-main {
  height: 100vh; /* 使用 100vh 来设置高度为全屏 */
  width: 100vw; /* 使用 100vw 来设置宽度为全屏 */
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: url('@/assets/bg.jpg');
  background-size: 100% 100%;
  background-repeat: no-repeat;

  .main-panel {
    background: #ffffff8f;
    border-radius: 20px;
    display: flex;
  }

  .panel-left {
    flex: 1;
    .left-image {
      padding: 40px;
    }
  }

  .panel-right {
    flex: 1;
    padding: 40px 80px 40px 40px;

    .panel-head {
      display: flex;
      align-items: center;
      margin-bottom: 40px;

      .head-line-left {
        background: linear-gradient(to right, #fff, #4695ff);
        height: 1px;
        flex: 1;
      }

      .head-line-right {
        background: linear-gradient(to right, #4695ff, #fff);
        height: 1px;
        flex: 1;
      }

      .head-title {
        color: #4695ff;
        font-weight: bold;
        font-size: 24px;
      }
    }

    .panel-title {
      text-align: center;
      font-size: 24px;
      line-height: 40px;
      height: 40px;
      margin-bottom: 20px;
    }
  }
}

.login-btn {
  background: #409eff;
  text-align: center;
  line-height: 40px;
  border-radius: 20px;
  color: #fff;
  margin-bottom: 10px;
  cursor: pointer;
}

.register-btn {
  background: #fff;
  text-align: center;
  line-height: 40px;
  border-radius: 20px;
  color: #409eff;
  box-sizing: border-box;
  border: 1px solid #eeeeee;
  cursor: pointer;
}

.tip {
  color: #797979;
  margin-top: 10px;
  font-size: 12px;
  margin-bottom: 20px;
}

.inputLength {
  width: 300px;
}
</style>
