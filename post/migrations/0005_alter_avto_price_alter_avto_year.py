# Generated by Django 4.2.7 on 2023-12-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_avto_remove_post_owner_delete_mediauser_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avto',
            name='price',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='avto',
            name='year',
            field=models.IntegerField(default=15000),
        ),
    ]
