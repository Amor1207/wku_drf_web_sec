<template>
  <div>
    <h2>个人中心</h2>
    <el-row>
      <el-col :span="12">
        <h3>个人信息</h3>
        <el-form :model="userInfo" label-width="120px">
          <el-form-item label="用户名">
            <el-input v-model="userInfo.username" disabled></el-input>
          </el-form-item>
          <el-form-item label="邮箱">
            <el-input v-model="userInfo.email" disabled></el-input>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="12">
        <h3>修改密码</h3>
        <el-form :model="passwordForm" label-width="120px">
          <el-form-item label="原密码">
            <el-input type="password" v-model="passwordForm.oldPassword"></el-input>
          </el-form-item>
          <el-form-item label="新密码">
            <el-input type="password" v-model="passwordForm.newPassword"></el-input>
          </el-form-item>
          <el-form-item label="确认新密码">
            <el-input type="password" v-model="passwordForm.confirmNewPassword"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="changePassword">提交</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "UserCenter",
  data() {
    return {
      userInfo: {
        // 您应该使用 API 请求获取用户信息数据
        username: "exampleUser",
        email: "example@example.com"
      },
      passwordForm: {
        oldPassword: "",
        newPassword: "",
        confirmNewPassword: ""
      }
    };
  },
  methods: {
    changePassword() {
      console.log("修改密码表单提交：", this.passwordForm);
      // 在这里实现修改密码逻辑，例如通过 API 请求与后端进行交互
    }
  }
};
</script>

<style scoped>
/* 在这里根据您的实际需求调整样式 */
</style>
