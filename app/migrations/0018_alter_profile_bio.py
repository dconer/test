# Generated by Django 4.2.7 on 2023-11-20 19:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_websitemeta_about_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=ckeditor.fields.RichTextField(max_length=200),
        ),
    ]
