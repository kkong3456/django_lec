# Generated by Django 3.2.7 on 2021-09-18 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='username',
            field=models.CharField(max_length=32, verbose_name='사용자명'),
        ),
    ]
