# Generated by Django 3.0.3 on 2020-05-02 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200502_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='media',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
