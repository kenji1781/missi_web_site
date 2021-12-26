# Generated by Django 3.2.9 on 2021-12-25 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_customer_machine_customer_machine_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine_model',
            name='Machine_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.equipment_category', verbose_name='装置カテゴリー'),
        ),
    ]
