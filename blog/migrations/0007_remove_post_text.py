# Generated by Django 4.0.6 on 2022-07-28 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
    ]