# Generated by Django 4.1.8 on 2023-07-25 19:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.TextField(blank=True, null=True, verbose_name="Título"),
        ),
    ]
