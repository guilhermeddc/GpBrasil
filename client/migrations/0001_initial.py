# Generated by Django 2.2.1 on 2019-08-05 22:51

import client.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChoicesCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
                'db_table': 'choices_city',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ChoicesCustomerService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_service', models.CharField(max_length=50, verbose_name='Tipos de atendimento')),
            ],
            options={
                'verbose_name': 'Atendimento',
                'verbose_name_plural': 'Atendimentos',
                'db_table': 'choices_customer_service',
                'ordering': ['customer_service'],
            },
        ),
        migrations.CreateModel(
            name='ChoicesEyeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=75, verbose_name='Cor')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em ')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em ')),
            ],
            options={
                'verbose_name': 'Cor',
                'verbose_name_plural': 'Cores',
                'db_table': 'choices_eye_color',
                'ordering': ['color'],
            },
        ),
        migrations.CreateModel(
            name='ChoicesGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50, verbose_name='Gênero')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em ')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em ')),
            ],
            options={
                'verbose_name': 'Gênero',
                'verbose_name_plural': 'Gêneros',
                'db_table': 'choices_genre',
                'ordering': ['genre'],
            },
        ),
        migrations.CreateModel(
            name='ChoicesPaymentAccepted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(max_length=50, verbose_name='Pagamento')),
            ],
            options={
                'verbose_name': 'Pagamento',
                'verbose_name_plural': 'Pagamentos',
                'db_table': 'choices_payment_accepted',
                'ordering': ['payment'],
            },
        ),
        migrations.CreateModel(
            name='ChoicesPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='Lugares')),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'Lugares',
                'db_table': 'choices_place',
                'ordering': ['place'],
            },
        ),
        migrations.CreateModel(
            name='ChoicesServicesOffered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', models.CharField(max_length=50, verbose_name='Serviços')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
                'db_table': 'choices_services_offered',
                'ordering': ['services'],
            },
        ),
        migrations.CreateModel(
            name='ChoicesStates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Nome')),
                ('uf', models.CharField(max_length=5, verbose_name='UF')),
            ],
            options={
                'verbose_name': 'UF',
                'verbose_name_plural': 'UF',
                'db_table': 'choices_states',
                'ordering': ['uf'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('slug', models.SlugField(max_length=30, verbose_name='Identificador')),
                ('description', models.TextField(max_length=250, verbose_name='Descrição')),
                ('age', models.PositiveIntegerField(verbose_name='Idade')),
                ('profile_picture', models.ImageField(blank=True, upload_to=client.models.upload_image_path, verbose_name='Foto do Perfil')),
                ('cacheForHours', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Cachê/Hr')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em ')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em ')),
            ],
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ethnicity', models.CharField(max_length=30, verbose_name='Etnia')),
                ('slug', models.SlugField(max_length=30, verbose_name='Identificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em ')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em ')),
            ],
            options={
                'verbose_name': 'Etnia',
                'verbose_name_plural': 'Etnias',
                'db_table': 'choices_ethnicity',
                'ordering': ['ethnicity'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to=client.models.upload_image_path, verbose_name='Videos')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
                'db_table': 'video',
                'ordering': ['client'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=client.models.upload_image_path, verbose_name='Fotos')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
                'db_table': 'photo',
                'ordering': ['client'],
            },
        ),
        migrations.CreateModel(
            name='InterClientActingCities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.ChoicesCity', verbose_name='Cidade')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Cidades em que atua',
                'verbose_name_plural': 'Cidades em que atua',
                'db_table': 'inter_client_acting_cities',
                'ordering': ['client'],
            },
        ),
        migrations.AddField(
            model_name='client',
            name='acting_cities',
            field=models.ManyToManyField(through='client.InterClientActingCities', to='client.ChoicesCity', verbose_name='Cidades de atuação'),
        ),
        migrations.AddField(
            model_name='client',
            name='customer_services',
            field=models.ManyToManyField(db_table='inter_client_customer_services', to='client.ChoicesCustomerService', verbose_name='Atendimentos'),
        ),
        migrations.AddField(
            model_name='client',
            name='ethnicity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Ethnicity', verbose_name='Etnia'),
        ),
        migrations.AddField(
            model_name='client',
            name='eye',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='client.ChoicesEyeColor', verbose_name='Olhos'),
        ),
        migrations.AddField(
            model_name='client',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.ChoicesGenre', verbose_name='Gênero'),
        ),
        migrations.AddField(
            model_name='client',
            name='payments_accepted',
            field=models.ManyToManyField(db_table='inter_client_payments_accepted', to='client.ChoicesPaymentAccepted', verbose_name='Pagamentos Aceitos'),
        ),
        migrations.AddField(
            model_name='client',
            name='places_accepted',
            field=models.ManyToManyField(db_table='inter_client_places_accepted', to='client.ChoicesPlace', verbose_name='Lugares Aceitos'),
        ),
        migrations.AddField(
            model_name='client',
            name='services_offered',
            field=models.ManyToManyField(db_table='inter_client_services_offered', to='client.ChoicesServicesOffered', verbose_name='Serviços Oferecidos'),
        ),
        migrations.AddField(
            model_name='choicescity',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.ChoicesStates', verbose_name='UF'),
        ),
    ]
