# Generated by Django 3.1.3 on 2020-12-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201211_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsetting',
            name='author',
            field=models.BooleanField(verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='postsetting',
            name='comment',
            field=models.BooleanField(verbose_name='comment'),
        ),
    ]