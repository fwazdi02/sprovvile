# Generated by Django 2.2 on 2019-04-16 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('icon', models.ImageField(blank=True, upload_to='uploads/image/icon')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('enable', 'Enabled'), ('disable', 'Disabled')], default='enable', max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, upload_to='uploads/image')),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='publish', max_length=100)),
                ('seo_keywords', models.CharField(max_length=200)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='blog.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=150)),
                ('body', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('spam', 'Spam'), ('publish', 'Publish')], default='publish', max_length=100)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog.Post')),
            ],
        ),
    ]
