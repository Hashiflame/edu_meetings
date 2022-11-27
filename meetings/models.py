from django.db import models

from users.models import User, StudentProfile
from phonenumber_field.modelfields import PhoneNumberField

MONTHS = {
    '1': 'JAN',
    '2': 'FEB',
    '3': 'MAR',
    '4': 'APR',
    '5': 'MAY',
    '6': 'JUN',
    '7': 'JUL',
    '8': 'AUG',
    '9': 'SEP',
    '10': 'OCT',
    '11': 'NOV',
    '12': 'DEC',
}


class Meeting(models.Model):
    mentor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=120,
        unique=True
    )
    description = models.CharField(
        max_length=240
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    image = models.ImageField(
        upload_to='meeting_images',
        default='default_meeting_image.jpg'
    ) # install Pillow
    content = models.TextField()
    location = models.CharField(
        max_length=150
    )
    holding_date = models.DateField()
    book_phone_num = PhoneNumberField()
    slug = models.SlugField()

    listeners = models.ManyToManyField(
        StudentProfile,
        blank=True,
        related_name='meetings'
    )

    def get_month_str(self):
        return MONTHS[str(self.holding_date.month)]

    class Meta:
        ordering = ('-pk',)


class Hours(models.Model):
    meeting = models.ForeignKey(
        Meeting,
        on_delete=models.CASCADE,
        related_name='hours'
    )

    class WeekDays(models.TextChoices):
        MONDAY = 'Monday'
        TUESDAY = 'Tuesday'
        WEDNESDAY = 'Wednesday'
        THURSDAY = 'Thursday'
        FRIDAY = 'Friday'
        SATURDAY = 'Saturday'
        SUNDAY = 'Sunday'

    start_day = models.CharField(
        max_length=60,
        choices=WeekDays.choices
    )
    end_day = models.CharField(
        max_length=60,
        choices=WeekDays.choices
    )
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name_plural = 'Hours'


class MeetingURL(models.Model):
    meeting = models.OneToOneField(
        Meeting,
        on_delete=models.CASCADE,
        related_name='urls'
    )
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    behance = models.URLField(null=True, blank=True)
