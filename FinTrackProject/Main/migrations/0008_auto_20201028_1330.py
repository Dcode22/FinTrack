# Generated by Django 3.1.2 on 2020-10-28 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Main', '0007_auto_20201028_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingpayment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incomeing_payments', to='Accounts.profile'),
        ),
        migrations.AlterField(
            model_name='outgoingpayment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_payments', to='Accounts.profile'),
        ),
    ]
