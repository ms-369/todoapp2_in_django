# Generated by Django 5.0.8 on 2024-08-20 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="desc",
            new_name="title",
        ),
    ]
