from django.db.models.signals import post_save
from django.dispatch import receiver

from core import models


@receiver(signal=post_save, sender=models.City, dispatch_uid='create_city_report', weak=False)
def create_city_report(instance, **kwargs):
    quantidade = models.City.objects.count()

    with open('cidades.txt', 'w') as arquivo:
        arquivo.write(f'Quantidade de cidades:\n{quantidade}\n')
