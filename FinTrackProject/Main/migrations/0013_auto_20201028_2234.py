# Generated by Django 3.1.2 on 2020-10-28 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_auto_20201028_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingpayment',
            name='bank_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incoming_payments', to='Main.bankaccount'),
        ),
        migrations.AlterField(
            model_name='incomingpayment',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='incomingpayment',
            name='income_source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incoming_payments', to='Main.incomesource'),
        ),
        migrations.AlterField(
            model_name='outgoingpayment',
            name='bank_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='outgoing_payments', to='Main.bankaccount'),
        ),
        migrations.AlterField(
            model_name='outgoingpayment',
            name='credit_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='outgoing_payments', to='Main.creditcard'),
        ),
        migrations.AlterField(
            model_name='outgoingpayment',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='outgoingpayment',
            name='merchant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='outgoing_payments', to='Main.merchant'),
        ),
    ]
