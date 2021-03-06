# Generated by Django 4.0.1 on 2022-03-13 14:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(blank=True, default=None, max_length=100, null=True, unique=True)),
                ('password', models.CharField(blank=True, default=None, max_length=128, null=True)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=255, null=True, verbose_name='E-Mail Address')),
                ('full_name', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Full Name')),
                ('country', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Province / State')),
                ('city', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='City')),
                ('zip', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='PPostal / Zip Code')),
                ('is_active', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'artweb_user',
            },
        ),
    ]
