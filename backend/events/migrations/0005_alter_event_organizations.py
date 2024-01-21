# Generated by Django 4.2.9 on 2024-01-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organizations", "0003_alter_membership_options_and_more"),
        ("events", "0004_alter_event_organizations"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="organizations",
            field=models.ManyToManyField(
                blank=True,
                related_name="events_organizations",
                to="organizations.organization",
                verbose_name="Организации",
            ),
        ),
    ]