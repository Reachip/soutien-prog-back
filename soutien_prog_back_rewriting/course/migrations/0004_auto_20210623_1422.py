# Generated by Django 3.2.4 on 2021-06-23 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("schoolmodule", "0001_initial"),
        ("course", "0003_auto_20210622_1426"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="school_module",
        ),
        migrations.AddField(
            model_name="course",
            name="school_module",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="schoolmodule.schoolmodule",
            ),
        ),
    ]
