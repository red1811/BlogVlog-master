# Generated by Django 2.2.7 on 2019-12-11 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('login', models.CharField(max_length=127, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=127, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]