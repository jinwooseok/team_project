# Generated by Django 3.2.14 on 2022-08-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0004_remove_count_post_user_confirm'),
    ]

    operations = [
        migrations.AddField(
            model_name='count_post',
            name='user_confirm',
            field=models.BooleanField(default=False),
        ),
    ]