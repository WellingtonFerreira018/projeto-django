# Generated by Django 4.1.7 on 2023-05-12 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_disc', '0003_interesse'),
    ]

    operations = [
        migrations.AddField(
            model_name='interesse',
            name='imagem',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]