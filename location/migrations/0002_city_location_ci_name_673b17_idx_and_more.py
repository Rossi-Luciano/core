# Generated by Django 4.1.10 on 2023-09-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("location", "0001_initial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="city",
            index=models.Index(fields=["name"], name="location_ci_name_673b17_idx"),
        ),
        migrations.AddIndex(
            model_name="country",
            index=models.Index(fields=["name"], name="location_co_name_22e724_idx"),
        ),
        migrations.AddIndex(
            model_name="country",
            index=models.Index(
                fields=["acronym"], name="location_co_acronym_46cf60_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="region",
            index=models.Index(fields=["name"], name="location_re_name_0b2832_idx"),
        ),
        migrations.AddIndex(
            model_name="region",
            index=models.Index(
                fields=["acronym"], name="location_re_acronym_386e65_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="state",
            index=models.Index(fields=["name"], name="location_st_name_45d2b5_idx"),
        ),
        migrations.AddIndex(
            model_name="state",
            index=models.Index(
                fields=["acronym"], name="location_st_acronym_2eca0b_idx"
            ),
        ),
    ]
