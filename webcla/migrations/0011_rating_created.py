# Generated by Django 4.1 on 2023-01-24 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("webcla", "0010_alter_rating_created_by_alter_rating_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
