# How to Enable Real Email Delivery

This guide will help you configure the attendance system to send real emails to students using Gmail or Outlook.

---

## Option 1: Gmail SMTP (Recommended)

### Step 1: Generate Gmail App Password

1. Go to your Google Account: https://myaccount.google.com/
2. Navigate to **Security** → **2-Step Verification** (enable it if not already enabled)
3. Scroll down to **App passwords**
4. Click **Select app** → Choose "Mail"
5. Click **Select device** → Choose "Other" and type "Django Attendance"
6. Click **Generate**
7. **Copy the 16-character password** (it will look like: `xxxx xxxx xxxx xxxx`)

### Step 2: Update Django Settings

Open `attendance_project/settings.py` and find the email configuration section (around line 120).

Replace the console backend with:

```python
# Email Configuration - Gmail SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # Replace with your Gmail address
EMAIL_HOST_PASSWORD = 'xxxx xxxx xxxx xxxx'  # Replace with your App Password
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'  # Replace with your Gmail address
```

### Step 3: Test It

1. Restart the Django server (stop and run `python manage.py runserver` again)
2. Login as a student
3. Click **"Email Me My Attendance"** button
4. Check your email inbox!

---

## Option 2: Outlook/Hotmail SMTP

### Step 1: Update Django Settings

Open `attendance_project/settings.py`:

```python
# Email Configuration - Outlook SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@outlook.com'  # Your Outlook email
EMAIL_HOST_PASSWORD = 'your-password'  # Your Outlook password
DEFAULT_FROM_EMAIL = 'your-email@outlook.com'
```

### Step 2: Test It

Restart the server and test the email feature.

---

## Option 3: Keep Console Email (Development Only)

If you want to see emails in the terminal without sending real ones:

```python
# Email Configuration - Console (Development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@attendancepro.com'
```

Emails will be printed in the terminal where `python manage.py runserver` is running.

---

## Troubleshooting

### Error: "SMTPAuthenticationError"
- **Gmail**: Make sure you generated an App Password (not your regular password)
- **Outlook**: Check if your account requires additional security settings

### Error: "SMTPServerDisconnected"
- Check your internet connection
- Verify EMAIL_PORT and EMAIL_HOST are correct

### Email Not Received
- Check spam/junk folder
- Verify the student's email address is correct in their profile
- Check terminal output for error messages

---

## Security Note

⚠️ **Never commit your `settings.py` with real passwords to GitHub or public repositories!**

For production, use environment variables:

```python
import os

EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
```

Then set them in your system:
- Windows: `set EMAIL_USER=your-email@gmail.com`
- Linux/Mac: `export EMAIL_USER=your-email@gmail.com`
