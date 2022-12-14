# Generated by Django 4.1.1 on 2022-11-26 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
