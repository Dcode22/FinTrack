# Generated by Django 3.1.2 on 2020-10-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Main', '0004_auto_20201027_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomecategory',
            name='profiles',
            field=models.ManyToManyField(blank=True, related_name='income_categories', to='Accounts.Profile'),
        ),
    ]
