import requests
from bs4 import BeautifulSoup
from linkedin_api import Linkedin
import os
from dotenv import load_dotenv

load_dotenv()

SEED_URL = 'https://www.linkedin.com/uas/login'
LOGIN_URL = 'https://www.linkedin.com/checkpoint/lg/login-submit'
VERIFY_URL = 'https://www.linkedin.com/checkpoint/challenge/verify'
LINKEDIN_USERNAME = os.getenv('LINKEDIN_USERNAME')
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')

session = requests.Session()


def login(email, password):
    session.get(SEED_URL)
    text = session.get(SEED_URL).text
    soup = BeautifulSoup(text, 'html.parser')
    payload = {'session_key': email,
               'loginCsrfParam': soup.find('input', {'name': 'loginCsrfParam'})['value'],
               'session_password': password}

    r = session.post(LOGIN_URL, data=payload)
    soup = BeautifulSoup(r.text, 'html.parser')

def GetLinkedInProfileData(linkedInURL):
    try:
        linkedInURLParts = linkedInURL.split('/')
        api = Linkedin(LINKEDIN_USERNAME, LINKEDIN_PASSWORD)
        profile = linkedInURLParts[len(linkedInURLParts)-1]
        return api.get_profile(profile)
    except Exception as e:
        return e
    
     