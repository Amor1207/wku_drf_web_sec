from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'avatars', views.AvatarViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'article', views.ArticleViewSet)

urlpatterns = [
    path('avatars/', views.AvatarViewSet.as_view({'get': 'list', 'post': 'create'}), name='avatar-list'),
    path('avatars/<int:pk>/', views.AvatarViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='avatar-detail'),
    path('categories/', views.CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('categories/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),
    path('tags/', views.TagViewSet.as_view({'get': 'list', 'post': 'create'}), name='tag-list'),
    path('tags/<int:pk>/', views.TagViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='tag-detail'),
    path('', views.ArticleViewSet.as_view({'get': 'list', 'post': 'create'}), name='article-list'),
    path('<int:pk>/', views.ArticleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='article-detail'),
    path('', include(router.urls)),
]

