# Generated by Django 2.0.2 on 2018-03-11 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20180222_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='id',
        ),
        migrations.AlterField(
            model_name='board',
            name='nombre',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]