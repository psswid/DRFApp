# Generated by Django 2.2.4 on 2019-10-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_auto_20191022_0638"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="pub_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
