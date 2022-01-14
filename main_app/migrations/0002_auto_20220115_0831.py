# Generated by Django 3.2.9 on 2022-01-14 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost_electric',
            name='Cost_id',
        ),
        migrations.RemoveField(
            model_name='cost_electric',
            name='Customer_machine_id',
        ),
        migrations.RemoveField(
            model_name='cost_electric',
            name='Customer_machine_unit_no',
        ),
        migrations.RemoveField(
            model_name='cost_electric',
            name='Customer_recipe_no',
        ),
        migrations.RemoveField(
            model_name='cost_electric',
            name='Data_date_day',
        ),
        migrations.RemoveField(
            model_name='cost_electric',
            name='Data_date_month',
        ),
        migrations.RemoveField(
            model_name='cost_electric',
            name='Data_date_year',
        ),
        migrations.RemoveField(
            model_name='cost_electric',
            name='Machine_model',
        ),
        migrations.RemoveField(
            model_name='cost_electric',
            name='Unit_price_electric',
        ),
        migrations.AlterField(
            model_name='cost_electric',
            name='Machine_drive_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cost_history_electric', to='main_app.machine_drive_history', verbose_name='稼働履歴'),
        ),
    ]
