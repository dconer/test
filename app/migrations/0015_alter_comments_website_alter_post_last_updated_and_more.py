# Generated by Django 4.2.7 on 2023-11-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='website',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Titulo'),
        ),
    ]
