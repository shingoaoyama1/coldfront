# Generated by Django 2.0.6 on 2018-08-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grant', '0003_auto_20180801_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='grant_pi_full_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
