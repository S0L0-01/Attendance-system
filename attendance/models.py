from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.roll_number} - {self.user.get_full_name()}"

    class Meta:
        ordering = ['roll_number']


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    total_classes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        ordering = ['code']


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.roll_number} - {self.subject.code} - {self.date} - {self.get_status_display()}"

    class Meta:
        ordering = ['-date']
        unique_together = ['student', 'subject', 'date']


class AttendancePercentage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='percentages')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='percentages')
    total_classes = models.IntegerField(default=0)
    classes_attended = models.IntegerField(default=0)
    percentage = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    last_updated = models.DateTimeField(auto_now=True)

    def calculate_percentage(self):
        if self.total_classes > 0:
            self.percentage = (self.classes_attended / self.total_classes) * 100
        else:
            self.percentage = 0.0
        self.save()

    def __str__(self):
        return f"{self.student.roll_number} - {self.subject.code} - {self.percentage:.2f}%"

    class Meta:
        unique_together = ['student', 'subject']
        ordering = ['student', 'subject']
