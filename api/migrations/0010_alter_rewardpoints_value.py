# Generated by Django 4.1 on 2022-08-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_rewardpoints_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewardpoints',
            name='value',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
