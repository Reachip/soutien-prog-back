# Generated by Django 3.2.4 on 2021-06-25 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20210623_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=80, null=True),
        ),
    ]