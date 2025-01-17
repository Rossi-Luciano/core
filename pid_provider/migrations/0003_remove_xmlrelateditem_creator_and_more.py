# Generated by Django 4.1.10 on 2023-08-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pid_provider", "0002_pidproviderxml_origin_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="xmlrelateditem",
            name="creator",
        ),
        migrations.RemoveField(
            model_name="xmlrelateditem",
            name="updated_by",
        ),
        migrations.RemoveIndex(
            model_name="pidchange",
            name="pid_provide_old_74f4ac_idx",
        ),
        migrations.RemoveIndex(
            model_name="pidchange",
            name="pid_provide_new_7260e5_idx",
        ),
        migrations.RemoveField(
            model_name="pidchange",
            name="new",
        ),
        migrations.RemoveField(
            model_name="pidchange",
            name="old",
        ),
        migrations.RemoveField(
            model_name="pidproviderxml",
            name="related_items",
        ),
        migrations.AddField(
            model_name="pidchange",
            name="pid_assigned",
            field=models.CharField(
                blank=True, max_length=23, null=True, verbose_name="PID assigned"
            ),
        ),
        migrations.AddField(
            model_name="pidchange",
            name="pid_in_xml",
            field=models.CharField(
                blank=True, max_length=23, null=True, verbose_name="PID pid_in_xml"
            ),
        ),
        migrations.AddField(
            model_name="pidchange",
            name="pkg_name",
            field=models.TextField(blank=True, null=True, verbose_name="Package name"),
        ),
        migrations.AddIndex(
            model_name="pidchange",
            index=models.Index(
                fields=["pid_in_xml"], name="pid_provide_pid_in__da2270_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="pidchange",
            index=models.Index(
                fields=["pid_assigned"], name="pid_provide_pid_ass_a06263_idx"
            ),
        ),
        migrations.DeleteModel(
            name="XMLRelatedItem",
        ),
    ]
