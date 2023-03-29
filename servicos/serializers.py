from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Prestador,Bairro,Subcategoria,Servico   

class PrestadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prestador
        fields = '__all__'

class BairroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bairro
        fields = '__all__'

    
class SubcategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subcategoria
        fields = '__all__'


class ServicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']