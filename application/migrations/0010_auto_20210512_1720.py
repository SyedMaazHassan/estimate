# Generated by Django 2.2.10 on 2021-05-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_auto_20210512_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base_values',
            name='warehouse_log_rate',
            field=models.IntegerField(verbose_name='Warehouse & Log OH Rate (% of Expenses)'),
        ),
    ]
