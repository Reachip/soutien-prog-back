# Generated by Django 3.2.4 on 2021-06-29 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_rename_link_to_course_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='link',
            new_name='link_to',
        ),
    ]