# Generated by Django 2.2.12 on 2020-04-24 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recentlypostlist',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.PostRoom', verbose_name='게시글'),
        ),
        migrations.AddField(
            model_name='recentlypostlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저'),
        ),
        migrations.AddField(
            model_name='contacttobroker',
            name='broker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Broker', verbose_name='공인중개사'),
        ),
        migrations.AddField(
            model_name='contacttobroker',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저'),
        ),
        migrations.AddField(
            model_name='user',
            name='brokers',
            field=models.ManyToManyField(through='members.ContactToBroker', to='posts.Broker'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='posts',
            field=models.ManyToManyField(through='members.RecentlyPostList', to='posts.PostRoom'),
        ),
        migrations.AddField(
            model_name='user',
            name='social',
            field=models.ManyToManyField(to='members.SocialLogin'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
