# Generated by Django 3.2.5 on 2022-03-16 14:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_delete_random'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user1',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user1',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user1',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]