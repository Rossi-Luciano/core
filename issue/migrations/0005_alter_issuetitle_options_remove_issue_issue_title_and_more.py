# Generated by Django 4.1.8 on 2023-05-29 20:11

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):
    dependencies = [
        ("issue", "0004_issue_city_issue_license_issue_sections_issuetitle_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="issuetitle",
            options={"ordering": ["sort_order"]},
        ),
        migrations.RemoveField(
            model_name="issue",
            name="issue_title",
        ),
        migrations.AddField(
            model_name="issuetitle",
            name="issue",
            field=modelcluster.fields.ParentalKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="issue_title",
                to="issue.issue",
            ),
        ),
        migrations.AddField(
            model_name="issuetitle",
            name="sort_order",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]