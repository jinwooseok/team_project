# Generated by Django 3.2.14 on 2022-08-24 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_count_post_user_confirm'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='count_post',
            options={'ordering': ('-user_dt',)},
        ),
    ]