# Generated by Django 4.1.8 on 2023-05-05 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("issue", "0003_issue_season_alter_issue_month_alter_issue_year"),
        ("article", "0005_documentabstract_remove_abstractmodel_keywords_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="pub_date_pub_year",
            new_name="pub_date_year",
        ),
        migrations.RemoveField(
            model_name="article",
            name="pub_date_collection",
        ),
        migrations.RemoveField(
            model_name="article",
            name="pub_date_collection_season",
        ),
        migrations.RemoveField(
            model_name="article",
            name="pub_date_collection_year",
        ),
        migrations.RemoveField(
            model_name="article",
            name="pub_date_pub",
        ),
        migrations.AddField(
            model_name="article",
            name="pub_date_day",
            field=models.CharField(
                blank=True,
                help_text="Dia de publicação no site.",
                max_length=10,
                null=True,
                verbose_name="pub date day",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="pub_date_month",
            field=models.CharField(
                blank=True,
                help_text="Mês de publicação no site.",
                max_length=10,
                null=True,
                verbose_name="pub date month",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="issue",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="issue.issue",
            ),
        ),
    ]