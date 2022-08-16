# Generated by Django 4.0.6 on 2022-08-16 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.BigAutoField(help_text='Comment ID', primary_key=True, serialize=False)),
                ('email', models.ForeignKey(db_column='post_id', on_delete=django.db.models.deletion.CASCADE, related_name='info', to='users.profile')),
            ],
        ),
    ]
