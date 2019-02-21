# Generated by Django 2.0.6 on 2019-02-21 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legs', models.IntegerField(default=0)),
                ('purpose', models.CharField(default='', max_length=1000)),
                ('purchaseTime', models.DateTimeField(default=datetime.datetime(2019, 2, 21, 15, 17, 30, 898508))),
            ],
        ),
    ]
