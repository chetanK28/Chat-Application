# Generated by Django 2.2.2 on 2019-06-22 04:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.SlugField(max_length=20)),
                ('group_info', models.CharField(blank=True, max_length=300, null=True)),
                ('creater', models.ForeignKey(on_delete=models.SET(home.models.get_sentinal_user), to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='all_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_info', models.CharField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to=home.models.get_image_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.TextField()),
                ('date_posted', models.DateTimeField(default=datetime.datetime.now)),
                ('parent_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='home.Group')),
                ('parent_user', models.ForeignKey(on_delete=models.SET(home.models.get_sentinal_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default_group.jpg', upload_to=home.models.get_group_image_path)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='group_profile', to='home.Group')),
            ],
        ),
    ]