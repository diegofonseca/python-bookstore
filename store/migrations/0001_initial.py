# Generated by Django 2.0.1 on 2018-01-22 02:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('publish_date', models.DateField(default=datetime.datetime(2018, 1, 22, 2, 0, 23, 415103, tzinfo=utc))),
            ],
        ),
    ]
