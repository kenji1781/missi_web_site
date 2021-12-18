# Generated by Django 3.2.8 on 2021-12-18 23:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cost_Electric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cost_electric', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='電力費用')),
                ('Data_date_year', models.IntegerField(blank=True, default=2021, null=True, validators=[django.core.validators.MinValueValidator(2021)], verbose_name='年')),
                ('Data_date_month', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='月')),
                ('Data_date_day', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)], verbose_name='日')),
                ('Data_datetime', models.DateTimeField(blank=True, null=True, verbose_name='データ取得日')),
                ('Machine_history_input_date', models.DateField(verbose_name='登録日')),
                ('Machine_history_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': '電力コスト',
            },
        ),
        migrations.CreateModel(
            name='Cost_Gas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cost_gas', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='ガス費用')),
                ('Data_date_year', models.IntegerField(blank=True, default=2021, null=True, validators=[django.core.validators.MinValueValidator(2021)], verbose_name='年')),
                ('Data_date_month', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='月')),
                ('Data_date_day', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)], verbose_name='日')),
                ('Data_datetime', models.DateTimeField(blank=True, null=True, verbose_name='データ取得日')),
                ('Machine_history_input_date', models.DateField(verbose_name='登録日')),
                ('Machine_history_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': 'ガスコスト',
            },
        ),
        migrations.CreateModel(
            name='Cost_Solvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cost_solvent', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='溶剤費用')),
                ('Data_date_year', models.IntegerField(blank=True, default=2021, null=True, validators=[django.core.validators.MinValueValidator(2021)], verbose_name='年')),
                ('Data_date_month', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='月')),
                ('Data_date_day', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)], verbose_name='日')),
                ('Data_datetime', models.DateTimeField(blank=True, null=True, verbose_name='データ取得日')),
                ('Machine_history_input_date', models.DateField(verbose_name='登録日')),
                ('Machine_history_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': '溶剤コスト',
            },
        ),
        migrations.CreateModel(
            name='Cost_Steam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cost_steam', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='蒸気費用')),
                ('Data_date_year', models.IntegerField(blank=True, default=2021, null=True, validators=[django.core.validators.MinValueValidator(2021)], verbose_name='年')),
                ('Data_date_month', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='月')),
                ('Data_date_day', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)], verbose_name='日')),
                ('Data_datetime', models.DateTimeField(blank=True, null=True, verbose_name='データ取得日')),
                ('Machine_history_input_date', models.DateField(verbose_name='登録日')),
                ('Machine_history_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': '蒸気コスト',
            },
        ),
        migrations.CreateModel(
            name='Customer_Infomation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(blank=True, max_length=20, verbose_name='企業名')),
                ('Customer_tel_number', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed.", regex='^[0-9]+$')], verbose_name='電話番号')),
                ('Customer_pastal_code', models.CharField(blank=True, max_length=7, null=True, validators=[django.core.validators.RegexValidator(message="Postal Code must be entered in the format: '1234567'. Up to 7 digits allowed.", regex='^[0-9]+$')], verbose_name='郵便番号')),
                ('Customer_address1', models.CharField(blank=True, max_length=40, null=True, verbose_name='都道府県')),
                ('Customer_address2', models.CharField(blank=True, max_length=40, null=True, verbose_name='市町村番地')),
                ('Customer_address3', models.CharField(blank=True, max_length=40, null=True, verbose_name='建物名')),
                ('Customer_input_date', models.DateField(verbose_name='登録日')),
                ('Customer_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': '客先情報',
            },
        ),
        migrations.CreateModel(
            name='Customer_Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_machine_id', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='装置ID')),
                ('Customer_machine_unit_no', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='号機')),
                ('Customer_machine_inst_date', models.DateField(blank=True, null=True, verbose_name='納入日')),
                ('Customer_machine_input_date', models.DateField(verbose_name='登録日')),
                ('Customer_machine_memo', models.TextField(blank=True, max_length=50, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': '客先装置',
            },
        ),
        migrations.CreateModel(
            name='Equipment_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipment_category', models.CharField(max_length=10, unique=True, verbose_name='装置カテゴリー')),
            ],
            options={
                'verbose_name_plural': '装置カテゴリー',
            },
        ),
        migrations.CreateModel(
            name='Machine_Drive_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_machine_id', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='装置ID')),
                ('Customer_recipe_no', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='品種No')),
                ('Machine_drive_time0', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='運転時間0')),
                ('Machine_drive_time1', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='運転時間1')),
                ('Machine_drive_time2', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='運転時間2')),
                ('Machine_drive_temp0', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度0')),
                ('Machine_drive_temp1', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度1')),
                ('Machine_drive_temp2', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度2')),
                ('Machine_drive_temp3', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度3')),
                ('Machine_drive_temp4', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度4')),
                ('Machine_drive_temp5', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度5')),
                ('Machine_drive_temp6', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度6')),
                ('Machine_drive_temp7', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度7')),
                ('Machine_drive_temp8', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度8')),
                ('Machine_drive_temp9', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度9')),
                ('Machine_drive_count', models.IntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='稼働回数')),
                ('Machine_water_used', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='水使用量')),
                ('Machine_steam_used', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='蒸気使用量')),
                ('Machine_electric_used', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='電力使用量')),
                ('Machine_gas_used', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='ガス使用量')),
                ('Data_date_year', models.IntegerField(blank=True, default=2021, null=True, validators=[django.core.validators.MinValueValidator(2021)], verbose_name='年')),
                ('Data_date_month', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='月')),
                ('Data_date_day', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)], verbose_name='日')),
                ('Data_datetime', models.DateTimeField(blank=True, null=True, verbose_name='データ取得日')),
                ('Machine_history_input_date', models.DateField(verbose_name='登録日')),
                ('Machine_history_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': '稼働履歴',
            },
        ),
        migrations.CreateModel(
            name='Mail_Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mail_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='氏名')),
                ('Mail_department', models.CharField(blank=True, max_length=20, null=True, verbose_name='部署')),
                ('Mail_address', models.EmailField(max_length=240)),
                ('Mail_input_date', models.DateField(blank=True, null=True, verbose_name='登録日')),
                ('Mail_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': '通知メール登録',
            },
        ),
        migrations.CreateModel(
            name='Recipe_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Recipe_id', models.IntegerField(blank=True, default=1, null=True, unique=True, verbose_name='品種ID')),
                ('Racipe_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='品種名')),
                ('Racipe_name_input_date', models.DateField(blank=True, null=True, verbose_name='登録日')),
                ('Racipe_name_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': 'レシピ情報',
            },
        ),
        migrations.CreateModel(
            name='Solvent_Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Solvent_name', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='溶剤名')),
                ('Solvent_name_input_date', models.DateField(verbose_name='登録日')),
            ],
            options={
                'verbose_name_plural': '溶剤名',
            },
        ),
        migrations.CreateModel(
            name='Trouble_Contents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trouble_no', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='異常No')),
                ('Trouble_contents', models.CharField(max_length=20, verbose_name='異常')),
                ('Trouble_input_date', models.DateField(verbose_name='登録日')),
                ('Trouble_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
                ('Machine_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.customer_machine', verbose_name='装置')),
            ],
            options={
                'verbose_name_plural': '異常内容',
            },
        ),
        migrations.CreateModel(
            name='Unit_Price_Electric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_price_electric', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='単価')),
                ('Unit_price_electric_input_date', models.DateField(verbose_name='登録日')),
                ('Unit_price_electric_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': '電力単価',
            },
        ),
        migrations.CreateModel(
            name='Unit_Price_Gas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_price_gas', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='単価')),
                ('Unit_price_gas_input_date', models.DateField(verbose_name='登録日')),
                ('Unit_price_gas_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': 'ガス単価',
            },
        ),
        migrations.CreateModel(
            name='Unit_Price_Steam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_price_steam', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='単価')),
                ('Unit_price_steam_input_date', models.DateField(verbose_name='登録日')),
                ('Unit_price_steam_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': '蒸気単価',
            },
        ),
        migrations.CreateModel(
            name='Unit_Price_Water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit_price_water', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='単価')),
                ('Unit_price_water_input_date', models.DateField(verbose_name='登録日')),
                ('Unit_price_water_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
            ],
            options={
                'verbose_name_plural': '水単価',
            },
        ),
        migrations.CreateModel(
            name='Trouble_Mail_Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trouble_mail_send_setting', models.BooleanField(verbose_name='送信設定')),
                ('Trouble_mail_input_date', models.DateField(blank=True, null=True, verbose_name='登録日')),
                ('Trouble_mail_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
                ('Trouble_contents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.trouble_contents', verbose_name='異常')),
                ('Trouble_mail_notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.mail_notification', verbose_name='メール設定')),
            ],
            options={
                'verbose_name_plural': '異常メール設定',
            },
        ),
        migrations.CreateModel(
            name='Trouble_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trouble_occurrence_time', models.DateTimeField(blank=True, null=True, verbose_name='発生時刻')),
                ('Trouble_recovery_time', models.DateTimeField(blank=True, null=True, verbose_name='復帰時刻')),
                ('Trouble_contents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.trouble_contents', verbose_name='異常')),
            ],
            options={
                'verbose_name_plural': '異常履歴',
            },
        ),
        migrations.CreateModel(
            name='Solvent_Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Solvent_manu', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='メーカー')),
                ('Solvent_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.solvent_name', verbose_name='溶剤')),
            ],
            options={
                'verbose_name_plural': '溶剤メーカー',
            },
        ),
        migrations.CreateModel(
            name='Solvent_Conf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Solvent_unit_price', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='単価')),
                ('Solvent_input_date', models.DateField(verbose_name='登録日')),
                ('Solvent_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
                ('Solvent_manu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.solvent_manufacturer', verbose_name='溶剤')),
            ],
            options={
                'verbose_name_plural': '溶剤設定',
            },
        ),
        migrations.CreateModel(
            name='Maintenance_Mail_Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maintenance_threshold', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='閾値')),
                ('Maintenance_send_setting', models.BooleanField(verbose_name='送信設定')),
                ('Maintenance_input_date', models.DateField(blank=True, null=True, verbose_name='登録日')),
                ('Maintenance_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
                ('Maintenance_machine_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.machine_drive_history', verbose_name='稼働履歴')),
                ('Maintenance_mail_notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.mail_notification', verbose_name='メール設定')),
            ],
            options={
                'verbose_name_plural': 'メンテナンスメール設定',
            },
        ),
        migrations.CreateModel(
            name='Machine_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Machine_model', models.CharField(max_length=20, verbose_name='型式')),
                ('Machine_model_input_date', models.DateField(verbose_name='登録日')),
                ('Machine_model_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
                ('Machine_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.equipment_category', verbose_name='装置カテゴリー')),
            ],
            options={
                'verbose_name_plural': '装置型式',
            },
        ),
        migrations.CreateModel(
            name='Customer_Machine_Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_recipe_no', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='品種No')),
                ('Customer_recipe_time0', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='運転時間設定0')),
                ('Customer_recipe_time1', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='運転時間設定1')),
                ('Customer_recipe_time2', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='運転時間設定2')),
                ('Customer_recipe_time3', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='運転時間設定3')),
                ('Customer_recipe_time4', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='運転時間設定4')),
                ('Customer_recipe_temp0', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度設定0')),
                ('Customer_recipe_temp1', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度設定1')),
                ('Customer_recipe_temp2', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度設定2')),
                ('Customer_recipe_temp3', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度設定3')),
                ('Customer_recipe_temp4', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度設定4')),
                ('Customer_recipe_temp5', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度設定5')),
                ('Customer_recipe_temp6', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度設定6')),
                ('Customer_recipe_temp7', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度設定7')),
                ('Customer_recipe_temp8', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度設定8')),
                ('Customer_recipe_temp9', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度設定9')),
                ('Customer_recipe_temp10', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度設定10')),
                ('Customer_recipe_temp11', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='温度設定11')),
                ('Customer_recipe_conf0', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定0')),
                ('Customer_recipe_conf1', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定1')),
                ('Customer_recipe_conf2', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定2')),
                ('Customer_recipe_conf3', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定3')),
                ('Customer_recipe_conf4', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定4')),
                ('Customer_recipe_conf5', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定5')),
                ('Customer_recipe_conf6', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定6')),
                ('Customer_recipe_conf7', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定7')),
                ('Customer_recipe_conf8', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定8')),
                ('Customer_recipe_conf9', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定9')),
                ('Customer_recipe_conf10', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定10')),
                ('Customer_recipe_conf11', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定11')),
                ('Customer_recipe_conf12', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定12')),
                ('Customer_recipe_conf13', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定13')),
                ('Customer_recipe_conf14', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定14')),
                ('Customer_recipe_conf15', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定15')),
                ('Customer_recipe_conf16', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定16')),
                ('Customer_recipe_conf17', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定17')),
                ('Customer_recipe_conf18', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定18')),
                ('Customer_recipe_conf19', models.CharField(blank=True, max_length=20, null=True, verbose_name='設定19')),
                ('Customer_machine_input_date', models.DateField(verbose_name='登録日')),
                ('Customer_machine_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
                ('Customer_machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.customer_machine', verbose_name='装置')),
                ('Customer_racipe_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.recipe_name', verbose_name='品種')),
            ],
            options={
                'verbose_name_plural': 'レシピ情報',
            },
        ),
        migrations.AddField(
            model_name='customer_machine',
            name='Machine_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.machine_model', verbose_name='装置'),
        ),
        migrations.CreateModel(
            name='Cost_Water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cost_water', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='水費用')),
                ('Data_date_year', models.IntegerField(blank=True, default=2021, null=True, validators=[django.core.validators.MinValueValidator(2021)], verbose_name='年')),
                ('Data_date_month', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='月')),
                ('Data_date_day', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)], verbose_name='日')),
                ('Data_datetime', models.DateTimeField(blank=True, null=True, verbose_name='データ取得日')),
                ('Machine_history_input_date', models.DateField(verbose_name='登録日')),
                ('Machine_history_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
                ('Machine_drive_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.machine_drive_history', verbose_name='稼働履歴')),
                ('Unit_price_water', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.unit_price_water', verbose_name='単価')),
            ],
            options={
                'verbose_name_plural': '水コスト',
            },
        ),
        migrations.CreateModel(
            name='Cost_Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cost_total', models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='合計費用')),
                ('Data_date_year', models.IntegerField(blank=True, default=2021, null=True, validators=[django.core.validators.MinValueValidator(2021)], verbose_name='年')),
                ('Data_date_month', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='月')),
                ('Data_date_day', models.IntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)], verbose_name='日')),
                ('Data_datetime', models.DateTimeField(blank=True, null=True, verbose_name='データ取得日')),
                ('Machine_history_input_date', models.DateField(verbose_name='登録日')),
                ('Machine_history_memo', models.TextField(blank=True, max_length=50, null=True, verbose_name='メモ')),
                ('Cost_electric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.cost_electric', verbose_name='電力費用')),
                ('Cost_gas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.cost_gas', verbose_name='ガス費用')),
                ('Cost_solvent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.cost_solvent', verbose_name='溶剤費用')),
                ('Cost_steam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.cost_steam', verbose_name='蒸気費用')),
                ('Cost_water', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.cost_water', verbose_name='水費用')),
                ('Machine_drive_history', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.machine_drive_history', verbose_name='稼働履歴')),
            ],
            options={
                'verbose_name_plural': 'トータルコスト',
            },
        ),
        migrations.AddField(
            model_name='cost_steam',
            name='Machine_drive_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.machine_drive_history', verbose_name='稼働履歴'),
        ),
        migrations.AddField(
            model_name='cost_steam',
            name='Unit_price_steam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.unit_price_steam', verbose_name='単価'),
        ),
        migrations.AddField(
            model_name='cost_solvent',
            name='Machine_drive_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.machine_drive_history', verbose_name='稼働履歴'),
        ),
        migrations.AddField(
            model_name='cost_solvent',
            name='Solvent_conf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.solvent_conf', verbose_name='単価'),
        ),
        migrations.AddField(
            model_name='cost_gas',
            name='Machine_drive_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.machine_drive_history', verbose_name='稼働履歴'),
        ),
        migrations.AddField(
            model_name='cost_gas',
            name='Unit_price_gas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.unit_price_gas', verbose_name='単価'),
        ),
        migrations.AddField(
            model_name='cost_electric',
            name='Machine_drive_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.machine_drive_history', verbose_name='稼働履歴'),
        ),
        migrations.AddField(
            model_name='cost_electric',
            name='Unit_price_electric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.unit_price_electric', verbose_name='単価'),
        ),
    ]
