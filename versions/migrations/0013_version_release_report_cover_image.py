# Generated by Django 4.2.16 on 2024-11-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("versions", "0012_review_reviewresult"),
    ]

    operations = [
        migrations.AddField(
            model_name="version",
            name="release_report_cover_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="release_report_cover/"
            ),
        ),
    ]