# Generated by Django 2.2.9 on 2021-03-31 17:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


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
                ('title', models.CharField(help_text='Title of group. Must not be empty.', max_length=200, unique=True)),
                ('slug', models.SlugField(help_text='Short name of Group for URL.', unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Group of posts',
                'verbose_name_plural': 'Groups of posts',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts2', to='posts.Group')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
