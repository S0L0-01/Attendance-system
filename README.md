# Student Attendance Management System (Django)

A comprehensive web application built with **Django** for tracking student attendance, calculating subject-wise percentages in real-time, and delivering detailed attendance summaries directly to students' registered emails.

---

## 🌟 Key Features

### 1. **Student Web Portal & Dashboard**
   - **Real-time Attendance Tracking**: Live subject-wise attendance percentage with color-coded progress bars
   - **Automatic Calculations**: Percentages update instantly via Django signals when attendance is marked
   - **Smart Alerts**: Visual warnings for subjects with attendance below 75%
   - **Overall Statistics**: Average attendance across all subjects with status indicators
   - **Detailed History**: View date-by-date attendance logs with Present/Absent/Late status and teacher remarks
   - **30-Day Calendar View**: Quick overview of recent attendance records

### 2. **Email Notification System**
   - **One-Click Email Reports**: Students can instantly send themselves a complete attendance summary
   - **Detailed Breakdown**: Email includes subject-wise attendance with percentages and class counts
   - **Warning Notifications**: Automatic alerts when overall attendance falls below 75%
   - **Flexible Configuration**: Switch between console (dev) and SMTP (production) via `email_config.py`

### 3. **User Registration & Authentication**
   - **Self-Service Registration**: Students can create accounts with roll number and email
   - **Form Validation**: Real-time error feedback with field-level validation messages
   - **Secure Authentication**: Password validation with Django's built-in security
   - **Automatic Profile Creation**: Student profile created automatically on registration

### 4. **Admin & Faculty Control Panel**
   - **Comprehensive Dashboard**: Manage all students, subjects, and attendance records
   - **Advanced Search**: Filter by roll number, name, date, subject, or status
   - **Bulk Operations**: Mark attendance for multiple students efficiently
   - **Auto-calculated Stats**: Attendance percentages update automatically across the system

---

## 🚀 Quick Start Guide

### 1. Launch the Application
From inside the `attendance_project` directory:
```bash
python manage.py runserver
```
Open your browser at **http://127.0.0.1:8000/**

### 2. Access the System

#### **Main Website:**
- Homepage: http://127.0.0.1:8000/
- Login: http://127.0.0.1:8000/login/
- Register: http://127.0.0.1:8000/register/

#### **Test Accounts:**

**Student Account (Pre-loaded with Sample Data):**
- **URL:** http://127.0.0.1:8000/login/
- **Username:** `student1`
- **Password:** `password123`
- **Features:** View dashboard, check attendance percentages, send email reports

**Admin/Faculty Account:**
- **URL:** http://127.0.0.1:8000/admin/
- **Username:** `admin`
- **Password:** `admin123`
- **Features:** Add students, manage subjects, mark daily attendance

---

## 📧 Email Configuration

### Current Setup (Default - Console Email)
By default, emails are printed to the terminal/console for testing purposes. When you click **"Email Me My Attendance"**, check your terminal window to see the email content.

### Enable Real Gmail Delivery

#### **Step 1: Generate Gmail App Password**
1. Visit: https://myaccount.google.com/apppasswords
2. Enable 2-Step Verification if not already enabled
3. Generate an App Password for "Django Attendance"
4. Copy the 16-character password (format: `xxxx xxxx xxxx xxxx`)

#### **Step 2: Update Configuration**
Open `attendance_project/email_config.py` and edit:

```python
EMAIL_CONFIG = {
    'BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'HOST': 'smtp.gmail.com',
    'PORT': 587,
    'USE_TLS': True,
    'HOST_USER': 'your-email@gmail.com',           # Your Gmail address
    'HOST_PASSWORD': 'your-16-char-app-password',  # App Password from Step 1
    'DEFAULT_FROM': 'your-email@gmail.com',        # Your Gmail address
}
```

#### **Step 3: Restart Server**
Stop the server (Ctrl+C) and restart:
```bash
python manage.py runserver
```

#### **For Outlook/Hotmail:**
```python
EMAIL_CONFIG = {
    'BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'HOST': 'smtp-mail.outlook.com',
    'PORT': 587,
    'USE_TLS': True,
    'HOST_USER': 'your-email@outlook.com',
    'HOST_PASSWORD': 'your-password',
    'DEFAULT_FROM': 'your-email@outlook.com',
}
```

**📄 Detailed Instructions:** See `EMAIL_SETUP_GUIDE.md` for troubleshooting and advanced configuration.

---

## 🎯 How to Use the System

### For Students:

1. **Register Your Account**
   - Go to http://127.0.0.1:8000/register/
   - Fill in your details (use your real email for attendance reports)
   - Create a username and secure password
   - Click "Create Account"

2. **View Your Dashboard**
   - Login with your credentials
   - See attendance percentages for all your subjects
   - Check which subjects have low attendance (below 75%)
   - View your overall average attendance

3. **Get Email Reports**
   - Click the green "Email Me My Attendance" button
   - Receive detailed breakdown of all subjects via email
   - Check console/terminal if using development mode

4. **View Detailed Logs**
   - Click "View Logs" on any subject card
   - See date-by-date attendance with remarks
   - Track Present/Absent/Late records

### For Faculty/Admin:

1. **Access Admin Panel**
   - Go to http://127.0.0.1:8000/admin/
   - Login with admin credentials

2. **Add New Students**
   - Click "Students" → "Add Student"
   - Link to existing user account or create new one
   - Enter roll number and email

3. **Create Subjects**
   - Click "Subjects" → "Add Subject"
   - Enter subject code, name, and description
   - Set total expected classes

4. **Mark Daily Attendance**
   - Click "Attendances" → "Add Attendance"
   - Select student and subject
   - Choose date and status (Present/Absent/Late)
   - Add optional remarks
   - **Percentages update automatically!**

---

## 🛠️ Project Structure

```text
attendance_project/
├── attendance/                      # Main Django app
│   ├── models.py                    # Database models (Student, Subject, Attendance, AttendancePercentage)
│   ├── views.py                     # View controllers (Dashboard, Login, Registration, Email)
│   ├── signals.py                   # Auto-calculation triggers for attendance percentages
│   ├── forms.py                     # Student registration form with validation
│   ├── urls.py                      # URL routing for all pages
│   ├── admin.py                     # Admin panel configuration
│   ├── apps.py                      # App configuration with signal registration
│   ├── templates/attendance/        # HTML templates
│   │   ├── base.html                # Base template with navigation
│   │   ├── home.html                # Landing page
│   │   ├── login.html               # Student login page
│   │   ├── register.html            # Student registration with error handling
│   │   ├── dashboard.html           # Main student dashboard with percentages
│   │   ├── subject_detail.html      # Individual subject attendance logs
│   │   └── calendar.html            # 30-day attendance history view
│   └── management/commands/         # Custom Django commands
│       └── populate_data.py         # Generate sample test data
├── attendance_project/              # Django project configuration
│   ├── settings.py                  # Main settings (reads email_config.py)
│   └── urls.py                      # Root URL configuration
├── static/css/                      # Static assets (CSS, JS, images)
├── email_config.py                  # Email provider configuration (editable)
├── EMAIL_SETUP_GUIDE.md             # Detailed email setup instructions
├── TESTING_GUIDE.md                 # Testing and usage guide
├── db.sqlite3                       # SQLite database (auto-generated)
├── manage.py                        # Django management script
└── README.md                        # This file
```

---

## 📊 Database Models

### **Student**
- Linked to Django User (one-to-one)
- Roll number (unique identifier)
- Email address (for attendance reports)
- Phone number (optional)

### **Subject**
- Subject code (e.g., CS101)
- Subject name
- Description
- Total classes count

### **Attendance**
- Student reference
- Subject reference
- Date of class
- Status: Present (P), Absent (A), or Late (L)
- Optional remarks from faculty

### **AttendancePercentage** (Auto-calculated)
- Student-Subject pair
- Total classes attended
- Total classes held
- Calculated percentage
- Last updated timestamp

---

## 🔧 Management Commands

### Populate Sample Data
Generate test students, subjects, and attendance records:
```bash
python manage.py populate_data
```

This creates:
- 1 sample student (student1/password123)
- 5 subjects (CS101, CS201, CS301, CS401, MATH101)
- 30 days of randomized attendance records

### Create Superuser (Admin)
Already created with credentials:
- Username: `admin`
- Password: `admin123`

To create additional admin accounts:
```bash
python manage.py createsuperuser
```

---

## 🔒 Security Notes

⚠️ **Important Security Reminders:**

1. **Never commit real passwords to Git:**
   - The `email_config.py` contains sensitive credentials
   - Add it to `.gitignore` before pushing to GitHub
   - Use environment variables for production

2. **Change default passwords:**
   - Update the admin password in production
   - Encourage students to use strong passwords

3. **Use HTTPS in production:**
   - The current setup is for development only
   - Deploy with SSL/TLS certificates in production

4. **Django SECRET_KEY:**
   - Generate a new secret key for production
   - Never share or commit the production secret key

---

## 🚀 Next Steps & Enhancements

### Ready-to-Add Features:
- **QR Code Attendance**: Students scan QR code to mark presence
- **Bulk CSV Upload**: Import attendance from Excel/CSV files
- **PDF Reports**: Download attendance as formatted PDFs
- **SMS Notifications**: Send alerts via Twilio
- **Parent Portal**: Allow parents to view student attendance
- **Mobile App**: React Native or Flutter mobile interface
- **Face Recognition**: Auto-mark attendance using camera
- **Geofencing**: Restrict attendance marking to campus location
- **Analytics Dashboard**: Visual charts and trends
- **Multi-semester Support**: Track attendance across terms

---

## 📞 Support & Documentation

- **Quick Testing:** See `TESTING_GUIDE.md`
- **Email Setup:** See `EMAIL_SETUP_GUIDE.md`
- **Django Documentation:** https://docs.djangoproject.com/

---

## 📅 Project Information

**Version:** 1.0  
**Last Updated:** September 12, 2026  
**Built With:** Django 6.1.1, Python 3.14.7, Bootstrap 5.3, SQLite  
**License:** MIT  

---

**🎉 Your attendance system is ready to use! Visit http://127.0.0.1:8000/ to get started.**
