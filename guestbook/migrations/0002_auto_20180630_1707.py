# Generated by Django 2.0.6 on 2018-06-30 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guestbook',
            old_name='contents',
            new_name='content',
        ),
    ]
