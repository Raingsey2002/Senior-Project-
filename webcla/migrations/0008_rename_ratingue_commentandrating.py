# Generated by Django 4.1 on 2023-01-21 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("webcla", "0007_ratingue"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="RatingUE",
            new_name="CommentandRating",
        ),
    ]