from django.contrib import admin
from django.utils.safestring import mark_safe

from users.models import MentorProfile
from .models import Meeting, Hours, MeetingURL


class HoursInline(admin.TabularInline):
    model = Hours


class MeetingURLInline(admin.StackedInline):
    model = MeetingURL


class MeetingConfig(admin.ModelAdmin):
    list_display = ['title', 'price', 'picture', 'listeners_count']
    inlines = [HoursInline, MeetingURLInline]

    def listeners_count(self, obj):
        return obj.listeners.count()

    def get_readonly_fields(self, request, obj=None):
        return ('mentor', 'listeners')

    def picture(self, obj):
        return mark_safe('<img src="{url}" width="50" height="50" />'.format(url=obj.image.url))

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug':  ("title",)}

    def save_model(self, request, obj, form, change):
        obj.mentor = request.user
        super().save_model(request, obj, form, change)

    # def _creator_permission(self, request, obj=None):
    #     if obj:
    #         return obj.mentor == request.user

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(mentor=request.user)
    #
    # has_delete_permission = _creator_permission
    # has_change_permission = _creator_permission


admin.site.register(Meeting, MeetingConfig)
