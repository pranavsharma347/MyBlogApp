# Generated by Django 3.0.7 on 2020-09-18 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=264),
            preserve_default=False,
        ),
    ]