# Generated by Django 2.1.2 on 2018-10-16 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20181014_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='contest_done',
            field=models.BooleanField(default=False),
        ),
    ]