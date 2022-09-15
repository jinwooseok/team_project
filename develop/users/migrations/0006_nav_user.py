# Generated by Django 3.2.14 on 2022-09-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='nav_user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('user_id', models.CharField(max_length=32, unique=True, verbose_name='유저 아이디')),
                ('user_name', models.CharField(max_length=16, verbose_name='유저 이름')),
                ('user_email', models.EmailField(max_length=128, verbose_name='유저 이메일')),
            ],
            options={
                'verbose_name': '네이버 로그인 유저',
                'verbose_name_plural': '네이버 로그인 유저',
                'db_table': 'nav_user',
            },
        ),
    ]