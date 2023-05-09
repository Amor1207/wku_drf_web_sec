<!-- src/components/ArticleList.vue -->
<template>
  <div>
    <el-row>
      <el-col :span="24">
        <h1>文章列表</h1>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <el-card v-for="article in articles" :key="article.id" class="article-card">
          <h3>{{ article.title }}</h3>
          <router-link :to="{ name: 'ArticleDetail', params: { id: article.id } }">查看详情</router-link>
        </el-card>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <h2>创建新文章</h2>
        <el-form @submit.prevent="createArticle">
          <el-form-item label="标题:">
            <el-input v-model="newArticle.title" required></el-input>
          </el-form-item>
          <el-form-item label="内容:">
            <el-input type="textarea" v-model="newArticle.content" required></el-input>
          </el-form-item>
          <el-form-item label="标签:">
            <el-select v-model="newArticle.tags" multiple placeholder="请选择标签">
              <el-option
                v-for="tag in tagOptions"
                :key="tag"
                :label="tag"
                :value="tag"
              />
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" native-type="submit">创建</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>


<script>
import api from '@/api';

export default {
  name: 'ArticleList',
  data() {
    return {
      articles: [],
      newArticle: {
        tags: [],
        title: "",
        body: "",
      },
      tagOptions: ["C", "C#", "C++", "Java", "Python"],
    };
  },
  async created() {
    try {
      const response = await api.getAllArticles();
      this.articles = response.data;
    } catch (error) {
      console.error('Error fetching articles:', error);
    }
  },
  methods: {
    async createArticle() {
      try {
        const response = await api.createArticle(this.newArticle);
        console.log("createArticle() called, response:", response.data);
        this.articles.unshift(response.data);
        this.newArticle = {
          tags: [],
          title: "",
          body: "",
        };
      } catch (error) {
        console.error("Error creating article:", error);
      }
      this.$forceUpdate();
    },
  },
};
</script>

<style scoped>
.article-card {
  margin-bottom: 20px;
}
</style>
