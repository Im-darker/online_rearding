# Generated by Django 2.2 on 2019-09-19 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='is_auth',
            field=models.BooleanField(default=False, verbose_name='是否认证'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='is_gold',
            field=models.BooleanField(default=False, verbose_name='是否为金牌'),
        ),
    ]
