# backend/skills/calendar_skill.py

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime, timedelta

class CalendarSkill:
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    
    def __init__(self):
        self.creds = None
        self.authenticate()

    def authenticate(self):
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SCOPES)
        self.creds = flow.run_local_server(port=0)

    def execute(self, params):
        event_name = params.get('event_name')
        start_time_str = params.get('start_time')  # Expecting ISO format
        duration = params.get('duration', 1)  # Duration in hours
        
        if not all([event_name, start_time_str]):
            return {'status': 'error', 'message': 'Missing event parameters.'}
        
        try:
            start_time = datetime.fromisoformat(start_time_str)
            end_time = start_time + timedelta(hours=int(duration))
            
            service = build('calendar', 'v3', credentials=self.creds)
            
            event = {
                'summary': event_name,
                'start': {'dateTime': start_time.isoformat(), 'timeZone': 'UTC'},
                'end': {'dateTime': end_time.isoformat(), 'timeZone': 'UTC'}
            }
            
            event_result = service.events().insert(calendarId='primary', body=event).execute()
            
            return {'status': 'success', 'message': f'Event "{event_result.get("summary")}" added to calendar.'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

calendar_skill = CalendarSkill()
