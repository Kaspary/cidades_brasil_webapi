# Generated by Django 2.2.1 on 2019-05-13 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='codigo_uf',
            new_name='code_uf',
        ),
    ]
