# Generated by Django 3.0.8 on 2020-08-12 15:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20200812_0239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionslot',
            name='hsm',
        ),
        migrations.AddField(
            model_name='sessionslot',
            name='msm',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10079)], verbose_name='minutes since monday at 12am (eastern time)'),
        ),
    ]
