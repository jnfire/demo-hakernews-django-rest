from app.api.models import News
from rest_framework import viewsets
from app.api.serializers import NewsSerializer
from rest_framework.response import Response


# Establezco una clase para el endpoint
class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver o editar las News.
    """
    # Conslta de los datos
    queryset = News.objects.all()
    def list(self, request):
        # Como se van a mostrar los datos
        serializer = NewsSerializer(self.queryset, many=True)
        return Response(serializer.data)

    # Función para hacer una actualización parcial de los datos
    def partial_update(self, request, pk=None):
        # Recuperamos la entrada queremos modificar
        my_news = News.objects.get(pk)
        # Actualizamos el campo que necesitamos
        my_news.votes = my_news.votes + 1
        # Guardamos el cambio
        my_news.save()
        # Formateamos en json
        serializer = News(my_news)
        return Response(serializer.data)
