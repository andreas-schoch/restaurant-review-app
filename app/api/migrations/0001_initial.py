# Generated by Django 2.0.3 on 2019-07-10 09:07

import api.helpers
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
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0, verbose_name='rating')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.Comment', verbose_name='Comment')),
                ('user_reacted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_reacted', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('category', models.CharField(choices=[('Asian', 'Asian'), ('Italian', 'Italian'), ('Swiss', 'Swiss'), ('Greek', 'Greek')], max_length=15)),
                ('country', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('zip', models.CharField(blank=True, max_length=30, null=True)),
                ('website', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('opening_hours', models.CharField(blank=True, max_length=30, null=True)),
                ('price_level', models.IntegerField(blank=True, null=True)),
                ('restaurant_pic', models.ImageField(blank=True, max_length=30, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('restaurant_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_restaurants', to=settings.AUTH_USER_MODEL, verbose_name='restaurant_owner')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('bio', models.CharField(blank=True, max_length=300)),
                ('interests', models.CharField(blank=True, max_length=30, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('code', models.CharField(default=api.helpers.generate_code, max_length=255, verbose_name='code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='api.Restaurant', verbose_name='Restaurant'),
        ),
        migrations.AlterUniqueTogether(
            name='reaction',
            unique_together={('user_reacted', 'comment')},
        ),
    ]
