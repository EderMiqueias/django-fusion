import uuid
from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField("Ativo?", default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engranagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-layers', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Nome', max_length=200)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Contribuinte(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField(
        'Imagem',
        upload_to=get_file_path,
        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}
    )
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('twitter', max_length=100, default='#')
    instagram = models.CharField('instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Contribuinte'
        verbose_name_plural = 'Contribuintes'

    def __str__(self):
        return self.nome


class Feature(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engranagem'),
        ('lni-rocket', 'Foguete'),
        ('lni-layers', 'Design'),
        ("lni-laptop-phone", "Laptop"),
        ("lni-leaf", "Folha")
    )
    feature = models.CharField('Feature', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.feature
