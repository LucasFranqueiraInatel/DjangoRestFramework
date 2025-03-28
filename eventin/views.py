from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Evento, Participante, Inscricao
from .serializers import (EventoSerializer, ParticipanteSerializer, InscricaoSerializer,
                          ListaIncricoesEventosSerializer, ListaInscricoesParticipantesSerializer, ParticipanteSerializerV2
                          )
from django_filters.rest_framework import DjangoFilterBackend

class EventoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Participante.objects.all()
    # serializer_class = ParticipanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return ParticipanteSerializerV2
        return ParticipanteSerializer

class InscricaoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer

class ListaIncricoesParticipante(generics.ListAPIView):
    serializer_class = ListaInscricoesParticipantesSerializer
    def get_queryset(self):
        queryset = Inscricao.objects.filter(participante_id=self.kwargs['pk'])
        return queryset

class ListaIncricoesEvento(generics.ListAPIView):
    serializer_class = ListaIncricoesEventosSerializer
    def get_queryset(self):
        queryset = Inscricao.objects.filter(evento_id=self.kwargs['pk'])
        return queryset