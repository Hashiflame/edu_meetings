# Generated by Django 4.1.3 on 2022-11-09 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_alter_meetingurl_meeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='holding_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 12, 12), null=True),
        ),
    ]
