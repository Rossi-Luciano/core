# Generated by Django 4.1.10 on 2023-09-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0002_article_issue_article_journal_article_keywords_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="first_page",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="last_page",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
