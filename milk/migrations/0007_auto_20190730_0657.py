# Generated by Django 2.2.3 on 2019-07-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milk', '0006_milkcategory_milk_company_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='milkcategory',
            name='milk_company_id',
        ),
        migrations.AddField(
            model_name='milkcategory',
            name='c_id',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
    ]
