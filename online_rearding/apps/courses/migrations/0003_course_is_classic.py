# Generated by Django 2.2 on 2019-09-19 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_classic',
            field=models.BooleanField(default=False, verbose_name='是否经典'),
        ),
    ]
