# Generated by Django 4.2.7 on 2023-12-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_avto_image_alter_avto_model_alter_avto_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avto',
            name='price',
            field=models.IntegerField(default=15000),
        ),
    ]
