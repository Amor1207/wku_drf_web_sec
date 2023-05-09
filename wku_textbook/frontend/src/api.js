// src/api.js
import axios from 'axios';

const httpClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api', // 根据你的 Django 服务器配置设置 baseURL
  timeout: 3000, // 请求超时时间
  headers: {
    'Content-Type': 'application/json',
  },
});

export default {
  // Avatar 接口
  getAllAvatars: () => httpClient.get('/article/avatars/'),
  createAvatar: (data) => httpClient.post('/article/avatars/', data),
  getAvatar: (id) => httpClient.get(`/article/avatars/${id}/`),
  updateAvatar: (id, data) => httpClient.put(`/article/avatars/${id}/`, data),
  deleteAvatar: (id) => httpClient.delete(`/article/avatars/${id}/`),

  // Category 接口
  getAllCategories: () => httpClient.get('/article/categories/'),
  createCategory: (data) => httpClient.post('/article/categories/', data),
  getCategory: (id) => httpClient.get(`/article/categories/${id}/`),
  updateCategory: (id, data) => httpClient.put(`/article/categories/${id}/`, data),
  deleteCategory: (id) => httpClient.delete(`/article/categories/${id}/`),

  // Tag 接口
  getAllTags: () => httpClient.get('/article/tags/'),
  createTag: (data) => httpClient.post('/article/tags/', data),
  getTag: (id) => httpClient.get(`/article/tags/${id}/`),
  updateTag: (id, data) => httpClient.put(`/article/tags/${id}/`, data),
  deleteTag: (id) => httpClient.delete(`/article/tags/${id}/`),

  // Article 接口
  getAllArticles: () => httpClient.get('/article/list_titles'), // 更新这里的URL
  createArticle: (data) => httpClient.post('/article/', data),
  async getArticle(id) {
    const response = await httpClient.get(`/article/${id}/`);
    return response.data;
  },
  updateArticle: (id, data) => httpClient.put(`/article/${id}/`, data),
  deleteArticle: (id) => httpClient.delete(`/article/${id}/`),

  // Comment 接口
  getComments: (articleId) => httpClient.get(`/article/${articleId}/comments/`),//issue
  submitComment: (articleId, content) => httpClient.post(`/article/${articleId}/comments/`, { content }),
};


