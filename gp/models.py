from random import randint
import os
from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils.utils import unique_slug_generator


class ChoicesEthnicity(models.Model):
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
    models.ManyToManyField('Client', through='InterClientActingCities')

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
    new_filename = randint(1, 9999)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'clients_photos/{new_filename}/{final_filename}'


class ClientQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)


class ClientManager(models.Manager):
    def get_queryset(self):
        return ClientQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):  # Client.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class Client(models.Model):
    featured = models.BooleanField('Evidencia', default=False)
    active = models.BooleanField('Ativo', default=True)

    first_name = models.CharField('nome', max_length=100)
    last_name = models.CharField('Sobrenome', max_length=100)
    slug = models.SlugField('Apelido', max_length=50, unique=True, blank=True)
    phone = models.CharField('Telefone', max_length=15, null=True, blank=True)
    whatsApp = models.CharField('WhatsApp', max_length=15, null=True, blank=True)
    email = models.EmailField('E-mail', max_length=100, null=True, blank=True)
    description = models.TextField('Descrição', max_length=250)
    shortDescription = models.TextField('Pequena descrição', max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField('Idade')
    image = models.ImageField('Foto do Perfil', upload_to=upload_image_path, null=True, blank=True)
    cacheForHours = models.DecimalField('Cachê/Hr', max_digits=6, decimal_places=2)
    weight = models.FloatField('Peso(kg)', null=True, blank=True)
    height = models.PositiveIntegerField('Altura(cm)', null=True, blank=True)
    bust = models.FloatField('Busto(cm)', null=True, blank=True)
    waist = models.FloatField('Cintura(cm)', null=True, blank=True)
    butt = models.FloatField('Bunda(cm)', null=True, blank=True)

    objects = ClientManager()

    # One to one relations
    genre = models.ForeignKey('ChoicesGenre', verbose_name='Gênero', on_delete=models.CASCADE)
    eye = models.ForeignKey('ChoicesEyeColor', verbose_name='Olhos', on_delete=models.CASCADE)
    ethnicity = models.ForeignKey('ChoicesEthnicity', verbose_name='Etnia', on_delete=models.CASCADE)

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

    class Meta:
        verbose_name = '$Cliente'
        verbose_name_plural = '$Clientes'
        ordering = ['-modified']

    def get_absolute_url(self):
        return f"/garotas/{self.slug}/"

    def __str__(self):
        return self.first_name + ' ' + self.last_name


def client_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(client_pre_save_receiver, sender=Client)


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
    client = models.ForeignKey('Client', verbose_name='Cliente', on_delete=models.DO_NOTHING, null=False, blank=False)
    city = models.ForeignKey('ChoicesCity', verbose_name='Cidade', on_delete=models.DO_NOTHING, null=False, blank=False)

    def __str__(self):
        return f'{self.client_id} {self.city_id}'

    class Meta:
        verbose_name = 'Cidades em que atua'
        verbose_name_plural = 'Cidades em que atua'
        ordering = ['client']
        db_table = 'inter_client_acting_cities'
        unique_together = ('client', 'city')
