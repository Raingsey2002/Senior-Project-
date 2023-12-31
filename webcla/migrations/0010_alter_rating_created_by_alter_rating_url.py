# Generated by Django 4.1 on 2023-01-23 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("webcla", "0009_rename_user_rating_created_by_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Ratings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="rating",
            name="url",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Ratings",
                to="webcla.website",
            ),
        ),
    ]
