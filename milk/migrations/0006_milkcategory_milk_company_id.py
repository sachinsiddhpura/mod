# Generated by Django 2.2.3 on 2019-07-30 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('milk', '0005_remove_subscription_milk_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='milkcategory',
            name='milk_company_id',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, to='milk.MilkCompany'),
            preserve_default=False,
        ),
    ]
