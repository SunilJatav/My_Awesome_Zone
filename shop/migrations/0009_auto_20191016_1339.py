# Generated by Django 2.2.6 on 2019-10-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20191016_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=3000),
        ),
    ]
