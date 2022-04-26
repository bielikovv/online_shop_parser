# Generated by Django 4.0.4 on 2022-04-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RozetkaSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('price', models.CharField(max_length=100, verbose_name='Price')),
                ('link', models.CharField(max_length=555, verbose_name='Link')),
                ('location', models.CharField(max_length=255, verbose_name='Location')),
                ('reviews', models.IntegerField(null=True, verbose_name='Reviews')),
            ],
        ),
    ]
