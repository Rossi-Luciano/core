# Generated by Django 4.1.10 on 2023-09-10 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("wagtaildocs", "0012_uploadeddocument"),
        ("vocabulary", "0002_alter_vocabulary_name"),
        ("reference", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
        ("journal", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="journal",
            name="name",
        ),
        migrations.RemoveField(
            model_name="journal",
            name="url",
        ),
        migrations.AddField(
            model_name="journal",
            name="abstract_language",
            field=models.ManyToManyField(
                related_name="abstract_language",
                to="core.language",
                verbose_name="Abstract Languages",
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="alphabet",
            field=models.CharField(
                blank=True,
                choices=[
                    ("A", "Basic Roman"),
                    ("B", "Extensive Roman"),
                    ("C", "Cirillic"),
                    ("D", "Japanese"),
                    ("E", "Chinese"),
                    ("K", "Korean"),
                    ("O", "Another alphabet"),
                ],
                max_length=4,
                null=True,
                verbose_name="Alphabet",
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="classification",
            field=models.TextField(
                blank=True, null=True, verbose_name="Classification"
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="frequency",
            field=models.CharField(
                blank=True,
                choices=[
                    ("?", "Unknown"),
                    ("A", "Annual"),
                    ("B", "Bimonthly (every two months)"),
                    ("C", "Semiweekly (twice a week)"),
                    ("D", "Daily"),
                    ("E", "Biweekly (every two weeks)"),
                    ("F", "Semiannual (twice a year)"),
                    ("G", "Biennial (every two years)"),
                    ("H", "Triennial (every three years)"),
                    ("I", "Three times a week"),
                    ("J", "Three times a month"),
                    ("K", "Irregular (known to be so)"),
                    ("M", "Monthly"),
                    ("Q", "Quarterly"),
                    ("S", "Semimonthly (twice a month)"),
                    ("T", "Three times a year"),
                    ("W", "Weekly"),
                    ("Z", "Other frequencies"),
                ],
                max_length=4,
                null=True,
                verbose_name="Frequency",
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="journal_url",
            field=models.URLField(blank=True, null=True, verbose_name="Journal Url"),
        ),
        migrations.AddField(
            model_name="journal",
            name="level_of_publication",
            field=models.CharField(
                blank=True,
                choices=[("CT", "Scientific/technical"), ("DI", "Divulgation")],
                max_length=2,
                null=True,
                verbose_name="Level of Publication",
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="medline_code",
            field=models.TextField(blank=True, null=True, verbose_name="Medline Code"),
        ),
        migrations.AddField(
            model_name="journal",
            name="medline_short_title",
            field=models.TextField(blank=True, null=True, verbose_name="Medline Code"),
        ),
        migrations.AddField(
            model_name="journal",
            name="national_code",
            field=models.TextField(blank=True, null=True, verbose_name="National Code"),
        ),
        migrations.AddField(
            model_name="journal",
            name="other_titles",
            field=models.ManyToManyField(
                to="reference.journaltitle", verbose_name="Other titles"
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="publishing_model",
            field=models.CharField(
                blank=True,
                choices=[("continuous", "Continuous"), ("undefined", "Undefined")],
                max_length=16,
                null=True,
                verbose_name="Publishing Model",
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="secs_code",
            field=models.TextField(blank=True, null=True, verbose_name="Secs Code"),
        ),
        migrations.AddField(
            model_name="journal",
            name="text_language",
            field=models.ManyToManyField(
                related_name="text_language",
                to="core.language",
                verbose_name="Text Languages",
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="treatment_level",
            field=models.CharField(
                blank=True,
                choices=[
                    ("am", "Analytical of a monograph"),
                    ("amc", "Analytical of a monograph in a collection"),
                    ("ams", "Analytical of a monograph in a serial"),
                    ("as", "Analytical of a serial"),
                    ("c", "Collective level"),
                    ("m", "Monographic level"),
                    ("mc", "Monographic in a collection"),
                    ("ms", "Monographic series level"),
                ],
                max_length=4,
                null=True,
                verbose_name="Treatment Level",
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="type_of_literature",
            field=models.CharField(
                blank=True,
                choices=[
                    ("C", "Conference"),
                    ("M", "Monograph"),
                    ("MC", "Conference papers as Monograph"),
                    ("MP", "Project papers as Monograph"),
                    ("MPC", "Project and Conference papers as monograph"),
                    ("MS", "Monograph Series"),
                    ("MSC", "Conference papers as Monograph Series"),
                    ("MSP", "Project papers as Monograph Series"),
                    ("N", "Document in a non conventional form"),
                    ("NC", "Conference papers in a non conventional form"),
                    ("NP", "Project papers in a non conventional form"),
                    ("P", "Project"),
                    ("S", "Serial"),
                    ("SC", "Conference papers as Periodical Series"),
                    ("SCP", "Conference and Project papers as periodical series"),
                    ("SP", "Project papers as Periodical Series"),
                    ("T", "Thesis and Dissertation"),
                    ("TS", "Thesis Series"),
                ],
                max_length=4,
                null=True,
                verbose_name="Type of Literature",
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="vocabulary",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="vocabulary.vocabulary",
            ),
        ),
        migrations.AddField(
            model_name="scielojournal",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("?", "Unknow"),
                    ("C", "Current"),
                    ("D", "Ceased"),
                    ("R", "Reports only"),
                    ("S", "Suspended"),
                ],
                max_length=12,
                null=True,
                verbose_name="Status",
            ),
        ),
        migrations.AlterField(
            model_name="journalsocialnetwork",
            name="name",
            field=models.TextField(
                blank=True,
                choices=[("facebook", "Facebook"), ("twitter", "Twitter")],
                null=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="scielojournal",
            name="name",
            field=models.TextField(
                blank=True,
                choices=[("facebook", "Facebook"), ("twitter", "Twitter")],
                null=True,
                verbose_name="Name",
            ),
        ),
        migrations.CreateModel(
            name="WebOfKnowledgeSubjectCategory",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                ("value", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="WebOfKnowledge",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                ("code", models.CharField(blank=True, max_length=8, null=True)),
                ("value", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SubjectDescriptor",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                ("value", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Subject",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                ("code", models.CharField(blank=True, max_length=30, null=True)),
                ("value", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Standard",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                ("code", models.CharField(blank=True, max_length=7, null=True)),
                ("value", models.TextField(blank=True, null=True)),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="IndexedAtFile",
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
                (
                    "is_valid",
                    models.BooleanField(
                        blank=True, default=False, null=True, verbose_name="Is valid?"
                    ),
                ),
                (
                    "line_count",
                    models.IntegerField(
                        blank=True, default=0, null=True, verbose_name="Number of lines"
                    ),
                ),
                (
                    "attachment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtaildocs.document",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IndexedAt",
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
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation date"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Last update date"
                    ),
                ),
                ("name", models.TextField(null=True, verbose_name="Name")),
                ("acronym", models.TextField(null=True, verbose_name="Acronym")),
                ("url", models.URLField(max_length=500, null=True, verbose_name="URL")),
                (
                    "description",
                    models.TextField(null=True, verbose_name="Description"),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("DATABASE", "DATABASE"),
                            ("DIRECTORY", "DIRECTORY"),
                            ("OTHER", "OTHER"),
                        ],
                        max_length=20,
                        null=True,
                        verbose_name="Type",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_creator",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Creator",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(class)s_last_mod_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Updater",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="journal",
            name="indexed_at",
            field=models.ManyToManyField(to="journal.indexedat"),
        ),
        migrations.AddField(
            model_name="journal",
            name="standard",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="journal.standard",
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="subject",
            field=models.ManyToManyField(
                to="journal.subject", verbose_name="Study Areas"
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="subject_descriptor",
            field=models.ManyToManyField(
                to="journal.subjectdescriptor", verbose_name="Subject Descriptors"
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="wos_area",
            field=models.ManyToManyField(
                to="journal.webofknowledgesubjectcategory",
                verbose_name="Web of Knowledge Subject Categories",
            ),
        ),
        migrations.AddField(
            model_name="journal",
            name="wos_db",
            field=models.ManyToManyField(
                to="journal.webofknowledge", verbose_name="Web of Knowledge Databases"
            ),
        ),
    ]
