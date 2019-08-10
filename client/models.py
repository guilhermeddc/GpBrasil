from random import randint
import os
from django.db import models


class Ethnicity(models.Model):
    ethnicity = models.CharField('Etnia', max_length=30)
    slug = models.SlugField('Identificador', max_length=30)

    class Meta:
        verbose_name = 'Etnia'
        verbose_name_plural = 'Etnias'
        ordering = ['ethnicity']
        db_table = 'choices_ethnicity'

    def __str__(self):
        return self.ethnicity


class ChoicesGenre(models.Model):
    genre = models.CharField('Gênero', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['genre']
        db_table = 'choices_genre'

    def __str__(self):
        return self.genre


class ChoicesEyeColor(models.Model):
    color = models.CharField('Cor', max_length=75, null=False, blank=False)

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'
        ordering = ['color']
        db_table = 'choices_eye_color'

    def __str__(self):
        return self.color


class ChoicesCustomerService(models.Model):
    customer_service = models.CharField('Tipos de atendimento', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
        ordering = ['customer_service']
        db_table = 'choices_customer_service'

    def __str__(self):
        return self.customer_service


class ChoicesPlace(models.Model):
    place = models.CharField('Lugares', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'
        ordering = ['place']
        db_table = 'choices_place'

    def __str__(self):
        return self.place


class ChoicesPaymentAccepted(models.Model):
    payment = models.CharField('Pagamento', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['payment']
        db_table = 'choices_payment_accepted'

    def __str__(self):
        return self.payment


class ChoicesServicesOffered(models.Model):
    services = models.CharField('Serviços', max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['services']
        db_table = 'choices_services_offered'

    def __str__(self):
        return self.services


class ChoicesStates(models.Model):
    name = models.CharField('Nome', max_length=75, null=False, blank=False)
    uf = models.CharField('UF', max_length=5, null=False, blank=False)

    class Meta:
        verbose_name = 'UF'
        verbose_name_plural = 'UF'
        ordering = ['uf']
        db_table = 'choices_states'

    def __str__(self):
        return self.uf


class ChoicesCity(models.Model):
    name = models.CharField('Nome', max_length=120, null=False, blank=False)

    # Many to One
    state = models.ForeignKey('ChoicesStates', verbose_name='UF', on_delete=models.CASCADE, null=False, blank=False)

    # Many to Many
    models.ManyToManyField('Client', through='client.models.InterClientActingCities')

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['name']
        db_table = 'choices_city'

    def __str__(self):
        return self.name


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = randint(1, 99999)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return 'clients_photos/{new_filename}/{final_filename}'.format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Client(models.Model):
    name = models.CharField('Nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)
    slug = models.SlugField('Identificador', max_length=30)
    description = models.TextField('Descrição', max_length=250)
    age = models.PositiveIntegerField('Idade')
    profile_picture = models.ImageField('Foto do Perfil', upload_to=upload_image_path, blank=True)
    cacheForHours = models.DecimalField('Cachê/Hr', max_digits=6, decimal_places=2)
    weight = models.FloatField('Peso(kg)', null=True, blank=True)
    height = models.FloatField('Altura(cm)', null=True, blank=True)
    bust = models.FloatField('Busto(cm)', null=True, blank=True)
    waist = models.FloatField('Cintura(cm)', null=True, blank=True)
    butt = models.FloatField('Bunda(cm)', null=True, blank=True)

    # One to one relations
    genre = models.ForeignKey('ChoicesGenre', verbose_name='Gênero', on_delete=models.CASCADE, null=False, blank=False)
    eye = models.ForeignKey('ChoicesEyeColor', verbose_name='Olhos', on_delete=models.CASCADE, null=False, blank=False,
                            default=True)
    ethnicity = models.ForeignKey('Ethnicity', verbose_name='Etnia', on_delete=models.CASCADE)

    # Many to many relations
    customer_services = models.ManyToManyField('ChoicesCustomerService',
                                               verbose_name='Atendimentos',
                                               db_table='inter_client_customer_services')

    places_accepted = models.ManyToManyField('ChoicesPlace',
                                             verbose_name='Lugares Aceitos',
                                             db_table='inter_client_places_accepted')

    payments_accepted = models.ManyToManyField('ChoicesPaymentAccepted',
                                               verbose_name='Pagamentos Aceitos',
                                               db_table='inter_client_payments_accepted')

    services_offered = models.ManyToManyField('ChoicesServicesOffered',
                                              verbose_name='Serviços Oferecidos',
                                              db_table='inter_client_services_offered')

    acting_cities = models.ManyToManyField('ChoicesCity',
                                           verbose_name='Cidades de atuação',
                                           through='InterClientActingCities')

    created = models.DateTimeField('Criado em ', auto_now_add=True)
    modified = models.DateTimeField('Modificado em ', auto_now=True)

    def __str__(self):
        return self.name + ' ' + self.last_name


class Photo(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField('Fotos', upload_to=upload_image_path, null=True, blank=True)
    title = models.CharField('Titulo', max_length=30, null=True, blank=True)
    description = models.CharField('descrição', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['client']
        db_table = 'photo'


class Video(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True, blank=True)
    video = models.FileField('Videos', upload_to=upload_image_path, null=True, blank=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        ordering = ['client']
        db_table = 'video'


# INTERMEDIATE MODELS
class InterClientActingCities(models.Model):
    client = models.ForeignKey('Client', verbose_name='Cliente', on_delete=models.CASCADE, null=False, blank=False)
    city = models.ForeignKey('ChoicesCity', verbose_name='Cidade', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = 'Cidades em que atua'
        verbose_name_plural = 'Cidades em que atua'
        ordering = ['client']
        db_table = 'inter_client_acting_cities'

    def __str__(self):
        return 'id: {0} - Nome: {1} - Cidade: {2} - UF: {3}'.format(self.client.pk,
                                                                    self.client.name,
                                                                    self.city.name,
                                                                    self.city.state.name)
