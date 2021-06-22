from app.api.models import News
from rest_framework import viewsets
from app.api.serializers import NewsSerializer

# Establezco una clase para el endpoint
class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint para ver o editar las News.
    """
    # Conslta de los datos
    queryset = News.objects.all()
    # Como se van a mostrar los datos
    serializer_class = NewsSerializer
