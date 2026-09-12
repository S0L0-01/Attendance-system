from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Attendance, AttendancePercentage

@receiver(post_save, sender=Attendance)
def update_attendance_on_save(sender, instance, **kwargs):
    """Automatically recalculate percentage when attendance is logged or modified"""
    student = instance.student
    subject = instance.subject

    total_classes = Attendance.objects.filter(student=student, subject=subject).count()
    classes_attended = Attendance.objects.filter(
        student=student,
        subject=subject,
        status__in=['P', 'L']  # Present and Late count as attended
    ).count()

    percentage_obj, created = AttendancePercentage.objects.get_or_create(
        student=student,
        subject=subject,
        defaults={
            'total_classes': total_classes,
            'classes_attended': classes_attended,
        }
    )

    percentage_obj.total_classes = total_classes
    percentage_obj.classes_attended = classes_attended
    percentage_obj.calculate_percentage()


@receiver(post_delete, sender=Attendance)
def update_attendance_on_delete(sender, instance, **kwargs):
    """Recalculate percentage when an attendance log is deleted"""
    student = instance.student
    subject = instance.subject

    total_classes = Attendance.objects.filter(student=student, subject=subject).count()
    classes_attended = Attendance.objects.filter(
        student=student,
        subject=subject,
        status__in=['P', 'L']
    ).count()

    try:
        percentage_obj = AttendancePercentage.objects.get(student=student, subject=subject)
        percentage_obj.total_classes = total_classes
        percentage_obj.classes_attended = classes_attended
        percentage_obj.calculate_percentage()
    except AttendancePercentage.DoesNotExist:
        pass
