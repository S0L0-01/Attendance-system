from django.contrib import admin
from .models import Student, Subject, Attendance, AttendancePercentage

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_number', 'get_full_name', 'email', 'created_at']
    search_fields = ['roll_number', 'user__first_name', 'user__last_name', 'email']
    list_filter = ['created_at']

    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Full Name'


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'total_classes', 'created_at']
    search_fields = ['code', 'name']
    list_filter = ['created_at']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'date', 'status', 'created_at']
    list_filter = ['status', 'date', 'subject']
    search_fields = ['student__roll_number', 'student__user__first_name', 'student__user__last_name']
    date_hierarchy = 'date'


@admin.register(AttendancePercentage)
class AttendancePercentageAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'total_classes', 'classes_attended', 'percentage', 'last_updated']
    list_filter = ['subject', 'last_updated']
    search_fields = ['student__roll_number', 'student__user__first_name', 'student__user__last_name']
    readonly_fields = ['percentage', 'last_updated']
