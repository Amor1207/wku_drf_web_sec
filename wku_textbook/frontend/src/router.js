import { createRouter, createWebHistory } from "vue-router";
import Home from './components/Home.vue';
import ArticleList from './components/ArticleList.vue';
import ArticleDetail from './components/ArticleDetail.vue';
import Textbook from './components/Textbook.vue';
import LoginRegister from './components/LoginRegister.vue';
import UserCenter from './components/UserCenter.vue';

const routes = [
  {
    path: '/',
    name: 'HomeComponent',
    component: Home
  },
  {
    path: '/article-list',
    name: 'ArticleList',
    component: ArticleList
  },
  {
    path: '/article-detail/:id',
    name: 'ArticleDetail',
    component: ArticleDetail,
    props: true,
  },
  {
    path: '/textbook',
    name: 'TextbookPage',
    component: Textbook
  },
  {
    path: '/login-register',
    name: 'LoginRegister',
    component: LoginRegister
  },
  {
    path: '/user-center',
    name: 'UserCenter',
    component: UserCenter
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;