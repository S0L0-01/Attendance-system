# ==============================================================================
# EMAIL CONFIGURATION TEMPLATE
# Copy this file to 'email_config.py' and fill in your real credentials.
# NOTE: 'email_config.py' is in .gitignore and will never be pushed to GitHub!
# ==============================================================================

# Option A: Gmail SMTP
# 1. Enable 2-Step Verification at https://myaccount.google.com/security
# 2. Generate an App Password at https://myaccount.google.com/apppasswords
# 3. Paste the 16-character App Password below

EMAIL_CONFIG = {
    'BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'HOST': 'smtp.gmail.com',
    'PORT': 587,
    'USE_TLS': True,
    'HOST_USER': 'your-email@gmail.com',
    'HOST_PASSWORD': 'your-16-char-app-password',
    'DEFAULT_FROM': 'your-email@gmail.com',
}

# Option B: Console Backend (Development Mode - prints to terminal)
# EMAIL_CONFIG = {
#     'BACKEND': 'django.core.mail.backends.console.EmailBackend',
#     'DEFAULT_FROM': 'noreply@attendancepro.com',
# }
