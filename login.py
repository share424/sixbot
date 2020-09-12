from bs4 import BeautifulSoup
import requests

def get_execution_code():
    print('[INFO] get execution code...')
    response = requests.get('https://login.itb.ac.id/cas/login?service=https%3A%2F%2Fakademik.itb.ac.id%2Flogin%2FINA')
    parsed_html = BeautifulSoup(response.text, features='html.parser')
    return parsed_html.body.find('input', attrs={'name': 'execution'})['value']

def login(nim, password):
    execution_code = get_execution_code()
    print('[INFO] login...')
    payload = {
        'username': nim, 
        'password': password, 
        'execution': execution_code,
        '_eventId': 'submit',
        'geolocation': None
    }
    session = requests.Session()
    log = session.post('https://login.itb.ac.id/cas/login?service=https%3A%2F%2Fakademik.itb.ac.id%2Flogin%2FINA', data=payload)
    if(log.status_code != 200):
        print('Wrong NIM or Password')
        return None
    return session
