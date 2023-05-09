<template>
  <div>
    <h2>教学资料</h2>
    <el-table :data="textbooks" style="width: 100%">
      <el-table-column prop="title" label="资料标题" width="180"></el-table-column>
      <el-table-column prop="author" label="作者" width="180"></el-table-column>
      <el-table-column prop="subject" label="科目" width="180"></el-table-column>
      <el-table-column prop="description" label="描述"></el-table-column>
      <el-table-column
        label="操作"
        width="120"
        fixed="right"
      >
        <template #default="{ row }">
          <el-button
            type="text"
            size="small"
            @click="openTextbookDetail(row.id)"
          >
            查看详情
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "TextbookPage",
  data() {
    return {
      textbooks: [
        // 在实际项目中，您应该通过 API 请求获取教学资料数据
        {
          id: 1,
          title: "教学资料1",
          author: "作者1",
          subject: "科目1",
          description: "教学资料1的描述"
        },
        {
          id: 2,
          title: "教学资料2",
          author: "作者2",
          subject: "科目2",
          description: "教学资料2的描述"
        },
        {
          id: 3,
          title: "教学资料3",
          author: "作者3",
          subject: "科目3",
          description: "教学资料3的描述"
        }
      ]
    };
  },
  methods: {
    openTextbookDetail(id) {
      console.log("查看教学资料详情，资料ID：", id);
      // 在这里实现查看教学资料详情的逻辑，例如跳转到教学资料详情页面
    }
  }
};
</script>

<style scoped>
/* 在这里根据您的实际需求调整样式 */
</style>