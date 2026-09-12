# Quick Start - Testing Registration & Email

## Test New Student Registration

1. Open your browser: http://127.0.0.1:8000/
2. Click **"Register"** in the top navigation
3. Fill in the form with your details:
   - **First Name**: Your first name
   - **Last Name**: Your last name
   - **Username**: Choose any username (e.g., `john_doe`)
   - **Roll Number**: Any format (e.g., `CS2026-999`)
   - **Email**: **YOUR REAL EMAIL ADDRESS** (where you want to receive attendance reports)
   - **Phone**: Optional
   - **Password**: At least 8 characters
   - **Confirm Password**: Same as above
4. Click **"Create Account"**
5. You should be automatically logged in and redirected to the dashboard

## After Registration

**Important**: You won't see any attendance data yet because:
- Faculty/Admin needs to add you to subjects
- Faculty/Admin needs to mark your attendance

### To Add Sample Data for Your New Account:

1. Login to Admin Panel: http://127.0.0.1:8000/admin/
   - Username: `admin`
   - Password: `admin123`

2. **Add Attendance for Your Account**:
   - Click on **"Attendances"**
   - Click **"Add Attendance"**
   - Select your student account
   - Select a subject (CS101, CS201, etc.)
   - Pick a date
   - Choose status (Present/Absent/Late)
   - Click **"Save and add another"** to add more records

3. Logout from admin and login as your student account to see the data!

## Enable Real Emails

By default, emails are printed to the console/terminal.

**To send to your real email**:
1. Follow the instructions in `EMAIL_SETUP_GUIDE.md`
2. Update `attendance_project/settings.py` with your Gmail credentials
3. Restart the server
4. Click "Email Me My Attendance" button on your dashboard
5. Check your inbox!

---

## Current Test Credentials

### Existing Student Account (with sample data):
- **Username**: `student1`
- **Password**: `password123`
- **Email**: `student1@example.com`

### Admin Account:
- **Username**: `admin`
- **Password**: `admin123`
- **URL**: http://127.0.0.1:8000/admin/
