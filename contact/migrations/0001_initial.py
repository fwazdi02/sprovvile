# Generated by Django 2.2 on 2019-04-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=150)),
                ('body', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
