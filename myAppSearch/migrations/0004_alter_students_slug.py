# Generated by Django 4.2.5 on 2023-09-15 04:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myAppSearch", "0003_alter_students_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="students",
            name="slug",
            field=models.SlugField(),
        ),
    ]