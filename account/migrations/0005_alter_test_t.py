# Generated by Django 4.2.1 on 2023-05-30 06:28

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_alter_test_t"),
    ]

    operations = [
        migrations.AlterField(
            model_name="test",
            name="t",
            field=jsonfield.fields.JSONField(default=[]),
        ),
    ]