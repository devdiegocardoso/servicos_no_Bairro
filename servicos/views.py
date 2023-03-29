from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, filters
from .serializers import PrestadorSerializer, BairroSerializer, SubcategoriaSerializer, ServicoSerializer, UserSerializer
from .models import Prestador, Bairro, Servico, Subcategoria
from django.contrib.auth.models import User
# Create your views here.

class PrestadorViewSet(viewsets.ModelViewSet):
    queryset =  Prestador.objects.all()
    serializer_class = PrestadorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        queryset =  Prestador.objects.all()
        bid = self.request.query_params.get('bairro_id', None)
        cid = self.request.query_params.get('categoria_id', None)
        uid = self.request.query_params.get('usuario_id', None)
        if bid is not None and cid is not None:
            queryset = Prestador.objects.filter(servicos=cid,bairros=bid)
        elif uid is not None:
            queryset = Prestador.objects.filter(user=uid)
        return queryset

class BairroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =  Bairro.objects.all()
    serializer_class = BairroSerializer

class ServicoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =  Servico.objects.all()
    serializer_class = ServicoSerializer

class SubcategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =  Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

    def get_queryset(self):
        queryset =  Subcategoria.objects.all()
        sid = self.request.query_params.get('servico_id', None)
        print(sid)
        if sid is not None:
            queryset = Subcategoria.objects.filter(servico_id=sid)
        return queryset

class UserViewSet(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

def index(request):
    return HttpResponse("Teste View")