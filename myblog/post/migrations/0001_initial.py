# Generated by Django 3.2.9 on 2021-11-05 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('shortdesc', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('location_lat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('location_lng', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(upload_to='uploads')),
                ('like', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
