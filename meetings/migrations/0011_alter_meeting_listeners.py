# Generated by Django 4.1.1 on 2022-11-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_password'),
        ('meetings', '0010_alter_meeting_listeners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='listeners',
            field=models.ManyToManyField(blank=True, to='users.studentprofile'),
        ),
    ]
