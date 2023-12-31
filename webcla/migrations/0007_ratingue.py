# Generated by Django 4.1 on 2023-01-21 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webcla", "0006_rename_website_rating_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="RatingUE",
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
                ("rating", models.PositiveSmallIntegerField()),
                ("comment", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
