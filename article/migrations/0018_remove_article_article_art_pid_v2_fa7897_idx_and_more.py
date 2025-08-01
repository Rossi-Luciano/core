# Generated by Django 5.0.8 on 2025-06-15 23:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0017_alter_articleformat_options_alter_article_created_and_more"),
        ("core", "0005_alter_language_options_alter_license_options_and_more"),
        ("doi", "0002_alter_doi_created_alter_doi_creator_and_more"),
        ("issue", "0004_alter_bibliographicstrip_created_and_more"),
        ("journal", "0038_alter_journal_options"),
        ("pid_provider", "0006_pidproviderxml_proc_status"),
        (
            "researcher",
            "0007_alter_affiliation_created_alter_affiliation_creator_and_more",
        ),
        ("vocabulary", "0004_alter_keyword_created_alter_keyword_creator_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="article",
            name="article_art_pid_v2_fa7897_idx",
        ),
        migrations.RemoveField(
            model_name="article",
            name="publisher",
        ),
        migrations.AddField(
            model_name="article",
            name="data_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("PUBLIC", "public"),
                    ("PENDING", "pending"),
                    ("MOVED", "moved"),
                    ("DELETED", "deleted"),
                    ("UNDEF", "undefined"),
                ],
                default="UNDEF",
                max_length=15,
                null=True,
                verbose_name="Data status",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="pp_xml",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="pid_provider.pidproviderxml",
            ),
        ),
        migrations.AddIndex(
            model_name="article",
            index=models.Index(fields=["valid"], name="article_art_valid_c853f2_idx"),
        ),
        migrations.AddIndex(
            model_name="article",
            index=models.Index(
                fields=["data_status"], name="article_art_data_st_07ece0_idx"
            ),
        ),
    ]
