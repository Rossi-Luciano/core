# Generated by Django 4.1.10 on 2023-09-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0002_article_issue_article_journal_article_keywords_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="article",
            index=models.Index(fields=["pid_v3"], name="article_art_pid_v3_2370cc_idx"),
        ),
        migrations.AddIndex(
            model_name="article",
            index=models.Index(
                fields=["pub_date_year"], name="article_art_pub_dat_9c64b4_idx"
            ),
        ),
    ]
