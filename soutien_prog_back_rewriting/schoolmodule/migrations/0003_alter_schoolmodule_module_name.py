# Generated by Django 3.2.4 on 2021-06-25 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmodule', '0002_alter_schoolmodule_module_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolmodule',
            name='module_name',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]