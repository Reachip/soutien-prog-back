# Generated by Django 3.2.4 on 2021-06-28 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_course_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='link',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
