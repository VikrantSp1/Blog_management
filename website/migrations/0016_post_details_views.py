# Generated by Django 4.0.3 on 2022-06-10 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_alter_post_details_blogcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_details',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
