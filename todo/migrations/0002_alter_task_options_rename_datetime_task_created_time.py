# Generated by Django 5.1.1 on 2024-09-25 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["is_done", "-created_time"]},
        ),
        migrations.RenameField(
            model_name="task",
            old_name="datetime",
            new_name="created_time",
        ),
    ]
