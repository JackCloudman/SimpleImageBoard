# Generated by Django 2.0.2 on 2018-03-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_post_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='board',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Titulo', max_length=50),
            preserve_default=False,
        ),
    ]
