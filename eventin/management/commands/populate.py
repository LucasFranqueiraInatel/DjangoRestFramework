import random
from django.core.management.base import BaseCommand
from faker import Faker
from eventin.models import Evento, Participante, Inscricao
from validate_docbr import CPF

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados fictícios'

    def handle(self, *args, **kwargs):
        fake = Faker(['pt_BR'])
        cpf_validator = CPF()

        eventos_titulos = [
            "Conferenência de Python",
            "Conferenência de Django",
            "Conferenência de JavaScript",
            "Workshop de Python",
            "Workshop de Django",
            "Workshop de JavaScript",
            "Seminário de Inteligência Artificial",
            "Seminário de Machine Learning",
            "Seminário de Deep Learning",
            "Palestra de Gestão de Projetos",
            "Palestra de Liderança",
        ]
        eventos = []
        for _ in range(10):
            evento = Evento(
                titulo=random.choice(eventos_titulos),
                descricao=fake.text(),
                local=fake.city(),
                data=fake.date_time_between(start_date='now', end_date='+30d'),
                capacidade=random.randint(10, 100),
            )
            eventos.append(evento)
        Evento.objects.bulk_create(eventos)

        participantes = []
        for _ in range(20):
            participante = Participante(
                nome=fake.name(),
                cpf=cpf_validator.generate(),
                email=fake.unique.email(),
                telefone=fake.phone_number(),
            )
            participantes.append(participante)
        Participante.objects.bulk_create(participantes)

        participantes_ids = Participante.objects.values_list('id', flat=True)
        eventos_ids = Evento.objects.values_list('id', flat=True)

        inscricoes = []
        for participantes_id in participantes_ids:
            for _ in range(random.randint(1, 3)):
                inscricao = Inscricao(
                    evento_id=random.choice(eventos_ids),
                    participante_id=participantes_id,
                )
                inscricoes.append(inscricao)
        Inscricao.objects.bulk_create(inscricoes)

        self.stdout.write(self.style.SUCCESS('Dados populados com sucesso!'))