# Generated by Django 5.0 on 2023-12-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("audiobatvoice", "0004_audio_audiosegment_delete_audiosegments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audiosegment",
            name="transcript",
            field=models.TextField(blank=True, null=True),
        ),
    ]