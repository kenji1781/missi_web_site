# Generated by Django 3.2.9 on 2021-11-25 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name_plural': '登録アカウント'},
        ),
    ]