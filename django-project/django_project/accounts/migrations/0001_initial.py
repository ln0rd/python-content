# Generated by Django 3.1.4 on 2021-01-26 12:35

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=60, unique=True, verbose_name='Nome do Usuário')),
                ('email', models.EmailField(max_length=140, unique=True, verbose_name='Email')),
                ('name', models.CharField(max_length=140, verbose_name='Nome Completo')),
                ('document', models.CharField(max_length=20, unique=True, verbose_name='Documento')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(blank=True, default=False, verbose_name='staff Status')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='joined date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]