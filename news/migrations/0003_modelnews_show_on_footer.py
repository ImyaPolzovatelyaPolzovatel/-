# Generated by Django 4.0.5 on 2022-07-06 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_modelnews_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelnews',
            name='show_on_footer',
            field=models.BooleanField(default=False, verbose_name='Показывать на футере'),
        ),
    ]
