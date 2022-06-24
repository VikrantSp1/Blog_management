# Generated by Django 4.0.3 on 2022-04-28 06:55

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
            name='Aboutproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img3', models.ImageField(upload_to='pics')),
                ('title3', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('client', models.CharField(max_length=100)),
                ('projDate', models.CharField(max_length=100)),
                ('fashiontitle', models.CharField(max_length=100)),
                ('fashiondes', models.CharField(max_length=100)),
                ('fashionContent', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='authorInsight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('title2', models.CharField(max_length=100)),
                ('list', models.CharField(max_length=100)),
                ('paragraph2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('icon', models.ImageField(upload_to='pics')),
                ('title', models.CharField(max_length=100)),
                ('paragraph', models.TextField()),
                ('url', models.CharField(max_length=100)),
                ('updatedOn', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='contactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=40)),
                ('subject', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='portfolios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img2', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('isactive', models.BooleanField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('url', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.categories')),
            ],
        ),
    ]
