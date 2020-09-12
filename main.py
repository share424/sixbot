from login import login
from profile import get_profile
from schedule import get_current_courses, check_course
from getpass import getpass

if __name__ == '__main__':
    nim = str(input('Student ID: '))
    password = str(getpass('Passowrd: '))

    session = login(nim, password)
    user_profile = get_profile(session)
    print('Welcome to SIX Bot')
    print('Your profile')
    print('Name :', user_profile['name'])
    print('NIM :', user_profile['nim'])
    print('Email :', user_profile['email'])

    courses = get_current_courses(session, user_profile['nim'])
    print(f'{len(courses)} found!')
    for course in courses:
        print(f'[INFO] checking {course["title"]}')
        check_course(session, course)