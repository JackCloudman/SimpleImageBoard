# Generated by Django 2.0.2 on 2018-02-22 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(upload_to='static'),
        ),
    ]
