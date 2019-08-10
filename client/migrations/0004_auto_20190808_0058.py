# Generated by Django 2.2.1 on 2019-08-08 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20190805_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='descrição'),
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='client',
            name='height',
            field=models.FloatField(blank=True, null=True, verbose_name='Altura(cm)'),
        ),
    ]
