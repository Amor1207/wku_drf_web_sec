<template>
  <div>
    <el-dialog
      v-model="dialogVisible"
      title="登录/注册"
      width="30%"
      @close="resetForm"
    >
      <el-tabs v-model="activeTab" @tab-click="handleTabClick">
        <el-tab-pane label="登录" name="login">
          <el-form :model="loginForm" ref="loginForm">
            <el-form-item label="用户名" prop="username">
              <el-input v-model="loginForm.username"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input type="password" v-model="loginForm.password"></el-input>
            </el-form-item>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="注册" name="register">
          <el-form :model="registerForm" ref="registerForm">
            <el-form-item label="用户名" prop="username">
              <el-input v-model="registerForm.username"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
              <el-input type="password" v-model="registerForm.password"></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="confirmPassword">
              <el-input type="password" v-model="registerForm.confirmPassword"></el-input>
            </el-form-item>
          </el-form>
        </el-tab-pane>
      </el-tabs>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="submitForm">提交</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: "LoginRegister",
  data() {
    return {
      dialogVisible: false,
      activeTab: "login",
      loginForm: {
        username: "",
        password: ""
      },
      registerForm: {
        username: "",
        password: "",
        confirmPassword: ""
      }
    };
  },
  methods: {
    handleTabClick(tab) {
      console.log("切换到", tab.label);
    },
    resetForm() {
      this.loginForm.username = "";
      this.loginForm.password = "";
      this.registerForm.username = "";
      this.registerForm.password = "";
      this.registerForm.confirmPassword = "";
    },
    submitForm() {
      if (this.activeTab === "login") {
        console.log("登录表单提交：", this.loginForm);
        // 在这里实现登录逻辑，例如通过 API 请求与后端进行交互
      } else {
        console.log("注册表单提交：", this.registerForm);
        // 在这里实现注册逻辑，例如通过 API 请求与后端进行交互
      }
    }
  }
};
</script>

