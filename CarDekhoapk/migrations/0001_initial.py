# Generated by Django 5.1.5 on 2025-02-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_price', models.IntegerField()),
                ('car_color', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('car_mileage', models.IntegerField()),
                ('car_description', models.TextField()),
                ('car_image', models.ImageField(upload_to='car_images')),
            ],
        ),
    ]
