# Generated by Django 3.2.4 on 2021-06-25 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0003_auto_20210623_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]