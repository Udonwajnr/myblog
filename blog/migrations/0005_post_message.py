# Generated by Django 4.0.6 on 2022-07-28 12:01

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_category_options_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='message',
            field=tinymce.models.HTMLField(default=2),
            preserve_default=False,
        ),
    ]
