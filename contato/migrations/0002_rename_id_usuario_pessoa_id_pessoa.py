# Generated by Django 4.2.3 on 2023-08-14 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='id_usuario',
            new_name='id_pessoa',
        ),
    ]
