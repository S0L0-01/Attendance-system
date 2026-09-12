from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count, Q
from .models import Student, Subject, Attendance, AttendancePercentage
from .forms import StudentRegistrationForm
from datetime import datetime, timedelta


def home(request):
    """Home page view"""
    return render(request, 'attendance/home.html')


def register(request):
    """Student registration view"""
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to the Attendance System.')
            return redirect('dashboard')
    else:
        form = StudentRegistrationForm()
    return render(request, 'attendance/register.html', {'form': form})


def user_login(request):
    """Login view"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'attendance/login.html', {'form': form})


def user_logout(request):
    """Logout view"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def dashboard(request):
    """Student dashboard showing attendance overview"""
    try:
        student = request.user.student
    except Student.DoesNotExist:
        messages.error(request, 'Student profile not found.')
        return redirect('home')

    # Get all attendance percentages for this student
    percentages = AttendancePercentage.objects.filter(student=student).select_related('subject')

    # Calculate overall statistics
    total_subjects = percentages.count()
    avg_attendance = sum(p.percentage for p in percentages) / total_subjects if total_subjects > 0 else 0

    # Get subjects below 75% (warning threshold)
    low_attendance = percentages.filter(percentage__lt=75)

    context = {
        'student': student,
        'percentages': percentages,
        'avg_attendance': avg_attendance,
        'total_subjects': total_subjects,
        'low_attendance': low_attendance,
    }

    return render(request, 'attendance/dashboard.html', context)


@login_required
def subject_detail(request, subject_id):
    """Detailed view of attendance for a specific subject"""
    try:
        student = request.user.student
    except Student.DoesNotExist:
        messages.error(request, 'Student profile not found.')
        return redirect('home')

    subject = get_object_or_404(Subject, id=subject_id)

    # Get attendance percentage
    try:
        percentage = AttendancePercentage.objects.get(student=student, subject=subject)
    except AttendancePercentage.DoesNotExist:
        percentage = None

    # Get all attendance records for this student and subject
    attendances = Attendance.objects.filter(
        student=student,
        subject=subject
    ).order_by('-date')

    context = {
        'student': student,
        'subject': subject,
        'percentage': percentage,
        'attendances': attendances,
    }

    return render(request, 'attendance/subject_detail.html', context)


@login_required
def send_attendance_email(request):
    """Send attendance summary email to student"""
    try:
        student = request.user.student
    except Student.DoesNotExist:
        messages.error(request, 'Student profile not found.')
        return redirect('home')

    # Get all attendance percentages
    percentages = AttendancePercentage.objects.filter(student=student).select_related('subject')

    # Create email content
    subject = 'Attendance Summary Report'
    message = f"Dear {student.user.get_full_name()},\n\n"
    message += f"Here is your attendance summary:\n\n"

    for p in percentages:
        message += f"{p.subject.code} - {p.subject.name}: {p.percentage:.2f}% ({p.classes_attended}/{p.total_classes} classes)\n"

    avg_attendance = sum(p.percentage for p in percentages) / percentages.count() if percentages.count() > 0 else 0
    message += f"\nOverall Attendance: {avg_attendance:.2f}%\n\n"

    if avg_attendance < 75:
        message += "⚠️ WARNING: Your attendance is below 75%. Please improve your attendance.\n\n"

    message += "Best regards,\nAttendance Management System"

    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [student.email],
            fail_silently=False,
        )
        messages.success(request, f'Attendance report sent to {student.email}')
    except Exception as e:
        messages.error(request, f'Failed to send email: {str(e)}')

    return redirect('dashboard')


@login_required
def attendance_calendar(request):
    """Calendar view of attendance"""
    try:
        student = request.user.student
    except Student.DoesNotExist:
        messages.error(request, 'Student profile not found.')
        return redirect('home')

    # Get attendance for the last 30 days
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=30)

    attendances = Attendance.objects.filter(
        student=student,
        date__range=[start_date, end_date]
    ).select_related('subject').order_by('-date')

    context = {
        'student': student,
        'attendances': attendances,
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, 'attendance/calendar.html', context)
