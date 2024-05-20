<template>
  <div class="login-wrap">
    <div class="login-main">
      <div class="main-panel">
        <div class="panel-left">
          <img src="@/assets/login.jpg" class="left-image" />
        </div>
        <div class="panel-right">
          <div class="panel-head">
            <div class="head-line-left"></div>
            <div class="head-title">黄河流域GDP分析系统 - 注册</div>
            <div class="head-line-right"></div>
          </div>
          <el-form :model="form" :rules="rules" ref="login">
            <el-form-item prop="id">
              <el-input v-model="form.id" placeholder="账号" class="inputLength">
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
            <el-form-item prop="cm_password">
              <el-input
                type="password"
                placeholder="再输入一次密码"
                v-model="form.cm_password"
                @keyup.enter="submitForm()"
                class="inputLength"
              >
                <el-icon><Key /></el-icon>
              </el-input>
            </el-form-item>
            <div class="tip">Tips : 请输入您的个人信息</div>
            <div class="tip-link" @click="this.$router.push('/login')">已有帐号？点击登录</div>
            <div class="login-btn" @click="submitForm()">注册</div>
          </el-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { User, Key } from '@element-plus/icons-vue'
import { register } from '@/api/Data'

export default {
  components: {
    User,
    Key
  },

  data: function () {
    return {
      form: {
        id: '',
        password: '',
        cm_password: ''
      }, //注册表单
      rules: {
        id: [
          { required: true, message: '请输入您的学号', trigger: 'blur' },
        ],
        password: [
          { required: true, message: '请输入您的密码', trigger: 'blur' }
        ],
        cm_password: [
          { required: true, message: '请再次输入密码', trigger: 'blur' },
          {
            validator: (rule, value, callback) => {
              if (value !== this.password) {
                callback(new Error('两次输入的密码不一致'))
              } else {
                callback()
              }
            },
            trigger: 'blur'
          }
        ]
      }
    };
  },

  methods: {
    //注册
    submitForm() {
      let params = {
        id: this.form.id,
        password: this.form.password,
        role: '学生'
      }
      register(params).then((res) => {
          let { data, status, msg } = res
          localStorage.setItem('user_info', JSON.stringify(data))
          if (status == '200') {
            this.$message.success('注册成功')
            this.$router.push('/teacher')
          } else {
            this.$message.error('注册失败:' + msg)
          }
      })
      .catch((error) => {
        this.$message.error('注册失败!' + error)
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
      height: 400px;
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
}
.tip-link {
  color: #2086ed;
  font-size: 12px;
  margin-bottom: 10px;
}

.inputLength {
  width: 300px;
}
</style>
