# Generated by Django 4.2.3 on 2023-07-26 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("location_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="placesmodel",
            name="user_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="User_Name",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]