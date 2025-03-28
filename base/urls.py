from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from eventin.views import EventoViewSet, ParticipanteViewSet, InscricaoViewSet, ListaIncricoesParticipante, ListaIncricoesEvento

router = routers.DefaultRouter()
router.register("eventos", EventoViewSet, basename="Eventos")
router.register("participantes", ParticipanteViewSet, basename="Participantes")
router.register("inscricoes", InscricaoViewSet, basename="Inscricoes")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('participantes/<int:pk>/inscricoes/', ListaIncricoesParticipante.as_view(), name='inscricoes-participante'),
    path('eventos/<int:pk>/inscricoes/', ListaIncricoesEvento.as_view(), name='inscricoes-evento'),
]
