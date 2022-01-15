# Generated by Django 3.2.9 on 2022-01-15 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20220116_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine_drive_history',
            name='Data_date',
            field=models.DateField(blank=True, null=True, verbose_name='データ取得日（年月日）'),
        ),
        migrations.AddField(
            model_name='machine_drive_history',
            name='Data_time',
            field=models.TimeField(blank=True, null=True, verbose_name='データ取得日（時分秒）'),
        ),
    ]
