# Generated by Django 3.2.9 on 2021-11-11 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['?'], 'verbose_name': 'تگ', 'verbose_name_plural': 'تگ ها '},
        ),
    ]