# Generated by Django 3.2.9 on 2021-11-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_auto_20211111_0819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['id'], 'verbose_name': 'تگ', 'verbose_name_plural': 'تگ ها '},
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=255, verbose_name='تاتیل'),
        ),
    ]
