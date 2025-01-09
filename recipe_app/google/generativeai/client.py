from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

class GenerativeAI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.service = build('generativeai', 'v1', developerKey=self.api_key)

    def generate_text(self, prompt):
        request = self.service.text().generate(prompt=prompt)
        response = request.execute()
        return response['text']