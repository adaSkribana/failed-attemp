# Generated by Django 5.0.4 on 2024-04-24 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myformsapp', '0002_alter_mymodel_field2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]