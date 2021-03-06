# Generated by Django 2.2.4 on 2020-03-18 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(default='Null', max_length=30)),
                ('password', models.CharField(max_length=16, verbose_name='password')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
