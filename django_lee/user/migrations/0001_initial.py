# Generated by Django 4.0.7 on 2022-08-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32, unique=True, verbose_name='유저 아이디')),
                ('user_pw', models.CharField(max_length=128, verbose_name='유저 비밀번호')),
                ('user_name', models.CharField(max_length=16, unique=True, verbose_name='유저 이름')),
                ('user_email', models.EmailField(max_length=128, unique=True, verbose_name='유저 이메일')),
                ('user_register_dttm', models.DateField(auto_now_add=True, verbose_name='계정 생성시간')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저',
                'db_table': 'user',
            },
        ),
    ]
