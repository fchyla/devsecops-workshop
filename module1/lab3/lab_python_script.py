#!/usr/bin/env python3
"""
DevOps Workshop Application
Lab File - Contains Test Secrets for Educational Purposes Only
"""

import os
import requests
import boto3
from flask import Flask, request, jsonify
import mysql.connector
import redis
import stripe

# WARNING: Never hardcode secrets in production!
# This is for lab demonstration purposes only

app = Flask(__name__)

# Database Configuration - INSECURE PRACTICE
DB_CONFIG = {
    'host': 'localhost',
    'user': 'workshop_user',
    'password': 'WorkshopDBPass2024!',  # VULNERABLE: Hardcoded password
    'database': 'workshop_db',
    'auth_plugin': 'mysql_native_password'
}

# Alternative connection string format
DATABASE_URL = "postgresql://postgres:PostgresPass123$@localhost:5432/workshop"

# API Keys and Secrets - INSECURE PRACTICE
AWS_CREDENTIALS = {
    'aws_access_key_id': 'AKIAIOSFODNN7EXAMPLE',
    'aws_secret_access_key': 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY'
}

# Stripe Payment Configuration
STRIPE_KEYS = {
    'publishable_key': 'pk_test_TYooMQauvdEDq54NiTphI7jx',
    'secret_key': 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'
}
stripe.api_key = STRIPE_KEYS['secret_key']

# Third-party Service Tokens
GITHUB_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1234567890"
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T1234567/B1234567/abcdefghijklmnopqrstuvwx"

# JWT Configuration
JWT_SECRET = "workshop_jwt_secret_key_2024_do_not_expose"
JWT_REFRESH_SECRET = "jwt_refresh_secret_workshop_2024"

# Redis Configuration
REDIS_PASSWORD = "RedisWorkshopPass2024#"
redis_client = redis.Redis(host='localhost', port=6379, password=REDIS_PASSWORD)

# Encryption Keys
ENCRYPTION_KEY = b'32_byte_key_for_AES_encryption_2024'
HMAC_SECRET = "hmac_secret_for_message_authentication_2024"

# Email Service Configuration
SMTP_CONFIG = {
    'server': 'smtp.gmail.com',
    'port': 587,
    'username': 'workshop@example.com',
    'password': 'GmailAppPassword123!'  # VULNERABLE: Hardcoded email password
}

# External API Keys
EXTERNAL_APIS = {
    'weather_api': 'api_key_1234567890abcdefghijklmnopqrstuv',
    'maps_api': 'AIzaSyD1234567890abcdefghijklmnopqrstuv',
    'sendgrid_api': 'SG.1234567890123456.abcdefghijklmnopqrstuvwxyz123456',
    'twilio_sid': 'AC1234567890abcdefghijklmnopqrstuv',
    'twilio_token': 'abcdef1234567890abcdef1234567890'
}

# OAuth Configuration
OAUTH_CONFIG = {
    'google': {
        'client_id': '123456789012-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com',
        'client_secret': 'GOCSPX-AbCdEfGhIjKlMnOpQrStUvWx'
    },
    'facebook': {
        'app_id': '1234567890123456',
        'app_secret': 'abcdefghijklmnopqrstuvwxyz123456'
    },
    'microsoft': {
        'tenant_id': '12345678-1234-1234-1234-123456789012',
        'client_id': '87654321-4321-4321-4321-210987654321',
        'client_secret': 'AbC~dEf1234567890_gHiJkLmNoPqRsTuV'
    }
}

# SSH Key for deployment (NEVER do this!)
DEPLOYMENT_SSH_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAACFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAgEA0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP
QRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWX
YZabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
-----END OPENSSH PRIVATE KEY-----"""

# SSL Certificate Private Key (Test Only)
SSL_PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC0123456789abcdef
ghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu
vwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
-----END PRIVATE KEY-----"""

def get_database_connection():
    """Get database connection using hardcoded credentials"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except mysql.connector.Error as error:
        print(f"Failed to connect to MySQL: {error}")
        return None

def send_notification(message):
    """Send notification to Slack"""
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    return response.status_code == 200

def upload_to_s3(file_path, bucket_name):
    """Upload file to S3 using hardcoded credentials"""
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_CREDENTIALS['aws_access_key_id'],
        aws_secret_access_key=AWS_CREDENTIALS['aws_secret_access_key']
    )
    
    try:
        s3_client.upload_file(file_path, bucket_name, os.path.basename(file_path))
        return True
    except Exception as e:
        print(f"S3 upload failed: {e}")
        return False

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "version": "1.0.0"})

@app.route('/config')
def get_config():
    # NEVER expose configuration like this in production!
    return jsonify({
        "database": DB_CONFIG['host'],
        "redis_configured": bool(REDIS_PASSWORD),
        "apis_configured": len(EXTERNAL_APIS)
    })

if __name__ == '__main__':
    # Development server configuration
    app.run(host='0.0.0.0', port=5000, debug=True)