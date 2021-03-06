# Generated by Django 2.2.4 on 2019-09-21 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('milk', '0009_auto_20190730_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('status', models.BooleanField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addtocartmilk', to='milk.Milk')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addtocart', to='milk.User')),
            ],
            options={
                'verbose_name': 'Add_To_Cart',
            },
        ),
    ]
