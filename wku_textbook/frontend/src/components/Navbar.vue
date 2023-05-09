<template>
  <el-menu mode="horizontal" :default-active="activeIndex" @select="handleSelect">
    <el-menu-item index="1" @click="goToHome">
      <i class="el-icon-s-home"></i>
      首页
    </el-menu-item>
    <el-menu-item index="2" @click="goToArticleList">
      <i class="el-icon-document"></i>
      文章
    </el-menu-item>
    <el-menu-item index="3" @click="goToTextbook" style="display: flex; align-items: center; justify-content: center;">
      <i class="el-icon-notebook-1"></i>
      教学资料
    </el-menu-item>
    <el-menu-item index="4" @click="goToUserCenter" v-if="loggedIn" style="display: flex; align-items: center; justify-content: center;">
      <i class="el-icon-user"></i>
      个人中心
    </el-menu-item>
    <div class="right-container">
      <div class="search-container">
        <el-input
          v-model="searchQuery"
          placeholder="搜索文章和教学资料"
          prefix-icon="el-icon-search"
          clearable
          @clear="clearSearch"
          @keyup.enter="performSearch"
        >
          <template #append>
            <el-button icon="el-icon-search" @click="performSearch"></el-button>
          </template>
        </el-input>
      </div>
      <el-menu-item index="5" @click="openLoginRegisterDialog" v-if="!loggedIn" style="display: flex; align-items: center; justify-content: center;">
        <i class="el-icon-user"></i>
        登录/注册
      </el-menu-item>
    </div>
  </el-menu>
  <login-register v-model:dialogVisible="showLoginRegisterDialog"></login-register>
</template>

<script>
import LoginRegister from "./LoginRegister.vue";

export default {
  name: "NavbarComponent",
  components: {
    LoginRegister
  },
  data() {
    return {
      activeIndex: "1",
      loggedIn: false, // 请根据实际情况更新用户登录状态
      showLoginRegisterDialog: false,
      searchQuery: ""
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    goToHome() {
      this.$router.push({ name: "HomeComponent" });
    },
    goToArticleList() {
      this.$router.push({ name: "ArticleList" });
    },
    goToTextbook() {
      this.$router.push({ name: "TextbookPage" });
    },
    goToUserCenter() {
      this.$router.push({ name: "UserCenter" });
    },
    openLoginRegisterDialog() {
      this.showLoginRegisterDialog = true;
    },
    clearSearch() {
      this.searchQuery = "";
    },
    performSearch() {
      console.log("执行搜索: ", this.searchQuery);
      // 在这里实现您的搜索逻辑
    }
  }
};
</script>

<style scoped>
.right-container {
  display: flex;
  align-items: center;
    margin-left: 80px;
}
.search-container {
  margin-right: 500px;
}
</style>
