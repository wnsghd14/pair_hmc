# Generated by Django 3.2.13 on 2022-10-28 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_tier'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]