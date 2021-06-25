from app.api.models import News
from rest_framework import viewsets, mixins
from app.api.serializers import NewsSerializer
from rest_framework.response import Response


class NewsViewSet( mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    """
    API endpoint that allows News to be viewed or edited.
    """
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    basename = "news"

    def get(self, request):
        serializer = NewsSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def put(self, request):
        # Update
        my_news = News.objects.get(pk=request.data['id'])
        my_news.votes = my_news.votes + 1
        my_news.save()
        # Devolvemos la noticia modificada
        serializer = NewsSerializer(my_news)
        return Response(serializer.data)
