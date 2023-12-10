# Generated by Django 4.2.6 on 2023-12-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("audiobatvoice", "0002_delete_audio_delete_audiosegments"),
    ]

    operations = [
        migrations.CreateModel(
            name="AudioSegments",
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
                ("audio_file", models.FileField(upload_to="static/media")),
                ("customer", models.CharField(max_length=30)),
                ("field", models.CharField(max_length=20)),
                ("status", models.CharField(default="new")),
                ("transcript", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
