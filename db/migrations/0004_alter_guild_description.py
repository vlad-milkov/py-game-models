# Generated by Django 4.0.2 on 2022-10-04 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_player_guild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
