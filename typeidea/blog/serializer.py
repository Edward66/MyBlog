from rest_framework import serializers, pagination

from django.contrib.auth.models import User

from .models import Post, Category, Tag


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # SlugRelatedField是用来配置外键数据的
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'  # 用来指定要展示的字段是什么
    )
    tag = serializers.SlugRelatedField(
        many=True,  # 因为是m2m
        read_only=True,
        slug_field='name',
    )
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    created_time = serializers.DateTimeField(format='%Y-%m-%d %X')

    class Meta:
        model = Post
        fields = (
            'url', 'id', 'title', 'category', 'tag', 'owner', 'created_time'
        )
        extra_kwargs = {
            'url': {'view_name': 'api-post-detail'},
        }


class PostDetailSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'category', 'tag', 'owner', 'content_html', 'created_time'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'url', 'id', 'name', 'created_time'
        )
        extra_kwargs = {
            'url': {'view_name': 'api-category-detail'},
        }


class CategoryDetailSerialiser(CategorySerializer):
    # SerializerMethodField帮我们把posts字段获取到的内容映射到paginated_posts
    posts = serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self, obj):
        posts = obj.post_set.filter(status=Post.STATUS_NORMAL)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(page, many=True, context={'request': self.context['request']})
        return {
            'count': posts.count(),
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'nett': paginator.get_next_link(),
        }

    class Meta:
        model = Category
        fields = (
            'id', 'name', 'created_time', 'posts'
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'url', 'id', 'name', 'created_time'
        )
        extra_kwargs = {
            'url': {'view_name': 'api-tag-detail'},
        }


class TagDetailSerializer(TagSerializer):
    posts = serializers.SerializerMethodField('paginated_posts')

    def paginated_posts(self, obj):
        posts = obj.post_set.filter(status=Tag.STATUS_NORMAL)
        paginator = pagination.PageNumberPagination()
        page = paginator.paginate_queryset(posts, self.context['request'])
        serializer = PostSerializer(page, many=True, context={'request': self.context['request']})
        return {
            'count': posts.count(),
            'results': serializer.data,
            'previous': paginator.get_previous_link(),
            'next': paginator.get_next_link(),
        }

    class Meta:
        model = Tag
        fields = (
            'id', 'name', 'created_time',
            'posts'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'url', 'id', 'username', 'post_set',
        )
        extra_kwargs = {
            'url': {'view_name': 'api-user-detail'},
        }


class UserDetailSerializer(UserSerializer):
    post_set = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'post_set',
        )
