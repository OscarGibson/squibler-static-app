# Generated by Django 2.1.1 on 2018-11-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_generator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='html',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
