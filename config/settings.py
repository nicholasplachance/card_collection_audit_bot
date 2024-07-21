# config/settings.py
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_password'
EMAIL_USE_TLS = True
RECIPIENT_EMAIL = 'recipient_email@example.com'

SPREADSHEET_ID = '1hXh3Y8xCA3XPtWQe5uL2ETIlaTNmfEKLWAmfR1Ypw1Y'
SHEET_NAME = 'Sheet1'

PRICE_THRESHOLD = {
    'week': 10.0,
    'month': 9.0
}
