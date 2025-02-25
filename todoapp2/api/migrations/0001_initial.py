# Generated by Django 5.0.8 on 2024-08-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("desc", models.CharField(max_length=200)),
                (
                    "completed",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
            ],
        ),
    ]
