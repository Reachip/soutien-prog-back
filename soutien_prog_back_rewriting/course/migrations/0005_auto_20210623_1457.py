# Generated by Django 3.2.4 on 2021-06-23 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("course", "0004_auto_20210623_1422"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="teacher",
        ),
        migrations.AddField(
            model_name="course",
            name="teacher",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
