# Generated by Django 3.2.8 on 2021-12-18 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solvent_name',
            name='Solvent_name_input_date',
            field=models.DateField(blank=True, null=True, verbose_name='登録日'),
        ),
        migrations.AlterField(
            model_name='equipment_category',
            name='Equipment_category',
            field=models.CharField(max_length=10, unique=True, verbose_name='装置カテゴリー'),
        ),
        migrations.AlterField(
            model_name='recipe_name',
            name='Recipe_id',
            field=models.IntegerField(blank=True, default=1, null=True, unique=True, verbose_name='品種ID'),
        ),
        migrations.AlterField(
            model_name='solvent_manufacturer',
            name='Solvent_manu',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='メーカー'),
        ),
        migrations.AlterField(
            model_name='solvent_name',
            name='Solvent_name',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='溶剤名'),
        ),
    ]
