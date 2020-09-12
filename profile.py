from bs4 import BeautifulSoup
import requests

def get_profile(session):
    print('[INFO] get user profile...')
    response = session.get('https://akademik.itb.ac.id/profile')
    parsed_html = BeautifulSoup(response.text, features='html.parser')
    tds = parsed_html.body.find_all('td')
    """
    Find Name

    selectors: body > div > div.row > div.col-md-5 > div > table > tbody > tr:nth-child(1) > td
    hacks: find first td
    """
    name = tds[0].decode_contents()
    
    """
    Find INA ID

    selectors: body > div > div.row > div.col-md-5 > div > table > tbody > tr:nth-child(2) > td
    hacks: find second td
    """
    nim = tds[1].decode_contents().strip()
    """
    Find Email

    selectors: body > div > div.row > div.col-md-5 > div > table > tbody > tr:nth-child(2) > td
    hacks: find fourth td
    """
    email = tds[3].decode_contents().strip()
    profile = {
        'name': name,
        'nim': nim,
        'email': email
    }
    return profile