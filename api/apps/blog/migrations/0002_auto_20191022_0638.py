# Generated by Django 2.2.6 on 2019-10-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='comments_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
    ]