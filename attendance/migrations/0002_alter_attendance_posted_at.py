# Generated by Django 4.1 on 2022-11-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='posted_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
