# Generated by Django 3.1.2 on 2020-11-03 15:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Main', '0030_auto_20201103_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incomecategory',
            name='profile',
        ),
        migrations.AddField(
            model_name='incomecategory',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='income_categories', to='Accounts.profile'),
        ),
        migrations.AlterField(
            model_name='incomingpayment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 3, 17, 1, 32, 542339)),
        ),
        migrations.AlterField(
            model_name='outgoingpayment',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 3, 17, 1, 32, 542339)),
        ),
    ]
