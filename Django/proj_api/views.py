from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from blog.models import Post


class ListPosts(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class ListSinglePost(APIView):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)
