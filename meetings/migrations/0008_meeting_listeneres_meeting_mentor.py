# Generated by Django 4.1.1 on 2022-11-26 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_is_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meetings', '0007_alter_meeting_options_alter_hours_meeting_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='listeneres',
            field=models.ManyToManyField(to='users.studentprofile'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='mentor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
