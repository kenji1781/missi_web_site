# Generated by Django 3.2.9 on 2022-01-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20220102_0518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_machine_recipe',
            name='Racipe_name',
        ),
        migrations.AddField(
            model_name='customer_machine_recipe',
            name='Recipe_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='品種名'),
        ),
    ]
