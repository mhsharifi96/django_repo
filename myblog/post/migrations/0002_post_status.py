# Generated by Django 3.2.9 on 2021-11-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('pub', 'publish'), ('drf', 'draft'), ('del', 'delete'), ('not', 'notset')], default='not', max_length=3),
        ),
    ]
