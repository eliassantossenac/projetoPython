# Generated by Django 4.2.3 on 2023-08-24 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0003_pessoa_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='img',
        ),
    ]
