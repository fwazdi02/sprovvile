# Generated by Django 2.2 on 2019-04-16 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='body',
            new_name='message',
        ),
    ]
