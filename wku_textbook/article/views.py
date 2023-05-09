from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from article.models import Article, Category, Tag, Avatar
from article.permissions import IsAdminUserOrReadOnly
from article.serializers import ArticleSerializer, CategorySerializer, TagSerializer, CategoryDetailSerializer, \
    ArticleDetailSerializer, AvatarSerializer


# Create your views here.
class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    @action(detail=False, methods=['get'])
    def list_titles(self, request, *args, **kwargs):
        articles = Article.objects.all()
        article_titles = [
            {
                "id": article.id,
                "title": article.title,
            }
            for article in articles
        ]
        return Response(article_titles)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.prefetch_related('articles')
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer
