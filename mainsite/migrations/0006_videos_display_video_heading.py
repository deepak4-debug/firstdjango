# Generated by Django 3.1.5 on 2021-07-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20210713_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='Display_Video_heading',
            field=models.BooleanField(default=False),
        ),
    ]
