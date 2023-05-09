<!-- src/components/ArticleDetail.vue -->
<template>
  <div>
    <el-page-header @back="$router.push({ name: 'HomeComponent' })" content="返回首页"></el-page-header>
    <el-card class="box-card mt-4 article-detail-card">
      <template v-slot:header>
        <h2 class="article-title">{{ article.title }}</h2>
      </template>
      <div class="article-body" v-html="article.body_html"></div>
    </el-card>
<!--    <el-form @submit.prevent="updateArticle" class="mt-4">-->
<!--      <el-form-item label="标题:">-->
<!--        <el-input v-model="article.title" placeholder="请输入文章标题"></el-input>-->
<!--      </el-form-item>-->
<!--      <el-form-item label="内容:">-->
<!--        <el-input type="textarea" v-model="article.body" placeholder="请输入文章内容"></el-input>-->
<!--      </el-form-item>-->
<!--&lt;!&ndash;      <el-form-item>&ndash;&gt;-->
<!--&lt;!&ndash;        <el-button type="primary" native-type="submit">更新</el-button>&ndash;&gt;-->
<!--&lt;!&ndash;        <el-button @click="deleteArticle" type="danger">删除文章</el-button>&ndash;&gt;-->
<!--&lt;!&ndash;      </el-form-item>&ndash;&gt;-->
<!--    </el-form>-->

    <h2 class="mt-4">评论</h2>
    <div v-for="comment in comments" :key="comment.id">
      <p><strong>{{ comment.author.username }}</strong> ({{ comment.created }})</p>
      <p>{{ comment.content }}</p>
      <hr>
    </div>
    <el-form @submit.prevent="submitComment" class="mt-4">
      <el-form-item label="添加评论:">
        <el-input type="textarea" v-model="newComment" placeholder="请输入评论内容"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" native-type="submit">提交评论</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import api from '@/api';

export default {
    name: 'ArticleDetail',
    props: {
        id: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            article: {
                title: '',
                content: '',
            },
            comments: [],
            newComment: '',
        };
    },
    async created() {
      const articleId = this.$route.params.id;

      try {
        this.article = await api.getArticle(articleId);

        const commentsResponse = await api.getComments(articleId);
        this.comments = commentsResponse.data.results;
      } catch (error) {
        console.error('Error fetching article:', error);
      }
    },

    methods: {
        async updateArticle() {
            try {
                const response = await api.updateArticle(this.id, this.article);
                this.article = response.data;
            } catch (error) {
                console.error('Error updating article:', error);
            }
        },
        async deleteArticle() {
            try {
                await api.deleteArticle(this.id);
                this.$router.push({name: 'Home'});
            } catch (error) {
                console.error('Error deleting article:', error);
            }
        },
        async submitComment() {
            try {
                await api.submitComment(this.id, this.newComment);
                const commentsResponse = await api.getComments(this.id);
                this.comments = commentsResponse.data.results;
                this.newComment = '';
            } catch (error) {
                console.error('Error submitting comment:', error);
            }
        },
    },
};
</script>

<style scoped>
.article-detail-card {
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.article-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 1rem;
}

.article-content {
  font-size: 16px;
  line-height: 1.6;
  text-align: justify;
}
</style>

