# Generated by Django 2.0.6 on 2018-07-04 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20180704_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='hit',
            field=models.IntegerField(default=0),
        ),
    ]
