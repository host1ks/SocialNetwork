from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response

from .models import Post, Like
from .serializers import PostSerializer, CreateLikesSerializer, ListLikeSerializer


class PostView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class LikeView(ListCreateAPIView):
    queryset = Like.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListLikeSerializer
        else:
            return CreateLikesSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        check = Like.objects.filter(**data)
        if check.exists():
            check.delete()
        else:
            ser = self.get_serializer(data=data)
            if ser.is_valid():
                ser.save()
        return Response(status=200)


class DetailLikeView(ListAPIView):
    serializer_class = ListLikeSerializer
    authentication_classes = []

    def get_queryset(self):
        return Like.objects.filter(
            date__range=[self.request.query_params.get('date_from'), self.request.query_params.get('date_to')])

    def get(self, request, *args, **kwargs):
        return Response({"count": len(self.get_queryset())})
