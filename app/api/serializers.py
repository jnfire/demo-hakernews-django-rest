from app.api.models import News
from rest_framework import serializers


# Establezco la clase de los datos qye va a entregar el api
class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # Establezco el modelo
        model = News
        # Establezco los campos que quiero ver
        fields = ['title', 'url', 'created']
