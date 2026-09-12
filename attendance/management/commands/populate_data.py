from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from attendance.models import Student, Subject, Attendance, AttendancePercentage
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the database with sample attendance data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')

        # Create subjects
        subjects_data = [
            {'code': 'CS101', 'name': 'Introduction to Programming', 'description': 'Basic programming concepts and Python'},
            {'code': 'CS201', 'name': 'Data Structures', 'description': 'Arrays, linked lists, trees, graphs'},
            {'code': 'CS301', 'name': 'Database Management', 'description': 'SQL, database design, normalization'},
            {'code': 'CS401', 'name': 'Web Development', 'description': 'HTML, CSS, JavaScript, Django'},
            {'code': 'MATH101', 'name': 'Calculus I', 'description': 'Limits, derivatives, integrals'},
        ]

        subjects = []
        for subj_data in subjects_data:
            subject, created = Subject.objects.get_or_create(
                code=subj_data['code'],
                defaults={
                    'name': subj_data['name'],
                    'description': subj_data['description'],
                    'total_classes': 40
                }
            )
            subjects.append(subject)
            if created:
                self.stdout.write(f'  Created subject: {subject.code}')

        # Create a sample student
        username = 'student1'
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username,
                password='password123',
                email='student1@example.com',
                first_name='John',
                last_name='Doe'
            )

            student = Student.objects.create(
                user=user,
                roll_number='CS2026-001',
                email='student1@example.com',
                phone='+1234567890'
            )
            self.stdout.write(f'  Created student: {student.roll_number}')

            # Generate attendance records for the past 30 days
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=30)

            for subject in subjects:
                # Randomly generate attendance for each subject
                attendance_percentage = random.uniform(0.65, 0.95)  # 65% to 95% attendance

                current_date = start_date
                while current_date <= end_date:
                    # Skip weekends
                    if current_date.weekday() < 5:  # Monday = 0, Friday = 4
                        # Randomly decide if there's a class on this day (70% chance)
                        if random.random() < 0.7:
                            # Determine status based on target percentage
                            if random.random() < attendance_percentage:
                                status = 'P' if random.random() < 0.95 else 'L'  # 95% present, 5% late
                            else:
                                status = 'A'

                            Attendance.objects.create(
                                student=student,
                                subject=subject,
                                date=current_date,
                                status=status,
                                remarks='Auto-generated sample data'
                            )

                    current_date += timedelta(days=1)

                self.stdout.write(f'  Generated attendance for {subject.code}')

            self.stdout.write(self.style.SUCCESS('\nSample data created successfully!'))
            self.stdout.write(self.style.SUCCESS(f'Login credentials: username={username}, password=password123'))
        else:
            self.stdout.write(self.style.WARNING('Sample student already exists. Skipping data creation.'))
