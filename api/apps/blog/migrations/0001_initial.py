# Generated by Django 2.2.6 on 2019-10-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('comments_count', models.IntegerField()),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]