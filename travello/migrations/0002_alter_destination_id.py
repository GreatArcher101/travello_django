# Generated by Django 4.2 on 2023-04-11 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
