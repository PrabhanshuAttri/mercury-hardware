# Generated by Django 2.2.10 on 2020-04-20 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mercury", "0018_remove_gfconfig_gf_db_grafana_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="gfconfig",
            name="gf_password",
            field=models.CharField(default="", max_length=128),
        ),
        migrations.AddField(
            model_name="gfconfig",
            name="gf_username",
            field=models.CharField(default="", max_length=128),
        ),
    ]
