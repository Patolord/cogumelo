# Generated by Django 2.1.7 on 2019-03-15 00:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=55)),
                ('subject', models.CharField(blank=True, max_length=65)),
                ('message', models.TextField()),
                ('contact_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
