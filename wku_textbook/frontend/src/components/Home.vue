<template>
  <div>
    <el-row>
      <el-col :span="12">
        <h2>最新文章</h2>
        <el-card v-for="article in latestArticles" :key="article.id" class="article-card">
          <h3>{{ article.title }}</h3>
          <p>{{ article.summary }}</p>
          <el-button type="text" @click="goToArticleDetail(article.id)">阅读更多</el-button>
        </el-card>
      </el-col>
      <el-col :span="12">
        <h2>热门话题</h2>
        <el-tag
          v-for="topic in hotTopics"
          :key="topic.id"
          closable
          @close="handleClose(topic)"
        >
          {{ topic.title }}
        </el-tag>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "HomeComponent",
  data() {
    return {
      latestArticles: [
        // 您应该使用 API 请求获取最新文章数据
        { id: 1, title: "WKU毕业“声” | 不到一个月拿下牛津offer，这个温肯女生早有“预谋"
            , summary: "日前，温州肯恩大学英语系大四学生梅寒冰收到了牛津大学教育学院教育理学硕士录取通知书。在2023QS世界排名中，牛津大学教育学科位列世界第五。从3月1日递交申请开始算起，不到一个月的时间，梅寒冰接连接到了牛津大学的材料初审、面试、录取的消息..." },
        { id: 2, title: "WKU毕业“声” | 卢长杰：两封直博全奖offer！这是个硬核追梦的故事"
            , summary: "今年温肯理工学院首位拿下全奖直博offer的学生，学校数学系成立以来直博第一人……来自数学系的大四毕业生卢长杰，目前接连收到了伊利诺伊大学香槟分校生物工程（生物医学影像分析方向）和卡内基梅隆大学与匹兹堡大学联培的计算生物专业的全奖博士offer..." },
        { id: 3, title: "WKU毕业“声” | 刘湘依：和生物细胞做朋友，科研女孩也浪漫"
            , summary: "接连拿下哥伦比亚大学、纽约大学、约翰霍普金斯大学三所名校Offer，获得浙江省政府奖学金、科研奖学金、院长一等奖学金，摘得多项生物、计算机奖项的刘湘依，用四年的探索和故事诠释了她学习生物的初心：在知识中找寻温度，用所学服务社会..." }
      ],
      hotTopics: [
        // 您应该使用 API 请求获取热门话题数据
        { id: 1, title: "话题1" },
        { id: 2, title: "话题2" },
        { id: 3, title: "话题3" }
      ],
      searchQuery: ""
    };
  },
  methods: {
    goToArticleDetail(id) {
      this.$router.push({ name: "ArticleDetail", params: { id } });
    },
    handleClose(topic) {
      console.log("关闭话题: ", topic.title);
    },
  }
};
</script>

<style scoped>
.article-card {
  margin-bottom: 20px;
}
.search-container {
  margin-top: 40px;
  text-align: center;
}
</style>

