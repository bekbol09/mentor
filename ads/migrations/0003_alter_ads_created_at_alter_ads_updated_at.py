# Generated by Django 4.2.4 on 2023-08-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_category_alter_ads_options_ads_created_at_ads_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
