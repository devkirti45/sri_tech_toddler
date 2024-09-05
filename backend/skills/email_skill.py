# backend/skills/email_skill.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSkill:
    def __init__(self):
        self.from_email = "youremail@example.com"
        self.password = "yourpassword"  # **Note:** Use environment variables for security

    def execute(self, params):
        to_email = params.get('to_email')
        subject = params.get('subject')
        message = params.get('message')
        
        if not all([to_email, subject, message]):
            return {'status': 'error', 'message': 'Missing email parameters.'}
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.from_email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.from_email, self.password)
            server.send_message(msg)
            server.quit()
            
            return {'status': 'success', 'message': f'Email sent to {to_email}!'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

email_skill = EmailSkill()
