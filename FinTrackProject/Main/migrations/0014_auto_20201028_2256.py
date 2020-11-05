# Generated by Django 3.1.2 on 2020-10-28 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0013_auto_20201028_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingpayment',
            name='income_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='incoming_payments', to='Main.incomesource'),
        ),
    ]