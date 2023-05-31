# Generated by Django 4.2.1 on 2023-05-30 06:25

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_remove_user_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="Test",
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
                ("t", jsonfield.fields.JSONField(default=[])),
            ],
        ),
    ]
