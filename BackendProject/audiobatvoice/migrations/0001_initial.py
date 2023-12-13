# Generated by Django 5.0 on 2023-12-13 09:43

import audiobatvoice.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Audio",
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
                ("title", models.CharField(max_length=50)),
                ("length", models.IntegerField(blank=True, null=True)),
                ("audio_file", models.FileField(upload_to="uploads/")),
                ("customer", models.CharField(max_length=30)),
                ("status", models.CharField(default="new", max_length=20)),
                ("timestamp", models.DateField(auto_now_add=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "anatator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AudioSegment",
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
                ("audio_file", models.FileField(upload_to="uploads/")),
                ("length", models.IntegerField(blank=True, null=True)),
                (
                    "transcript",
                    models.TextField(
                        blank=True,
                        default=" ",
                        null=True,
                        validators=[audiobatvoice.validators.check_character_set],
                    ),
                ),
                (
                    "audio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="audiobatvoice.audio",
                    ),
                ),
            ],
        ),
    ]
