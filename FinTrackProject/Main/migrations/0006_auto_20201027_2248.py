# Generated by Django 3.1.2 on 2020-10-27 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Main', '0005_auto_20201027_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomecategory',
            name='profiles',
            field=models.ManyToManyField(null=True, related_name='income_categories', to='Accounts.Profile'),
        ),
    ]