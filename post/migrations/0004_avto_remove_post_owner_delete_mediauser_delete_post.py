# Generated by Django 4.2.7 on 2023-12-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_post_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=1000)),
                ('about', models.TextField(blank=True)),
                ('year', models.IntegerField(default=2000)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
        migrations.DeleteModel(
            name='MediaUser',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
