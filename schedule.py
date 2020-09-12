from bs4 import BeautifulSoup

def get_current_courses(session, nim):
    print('[INFO] get current courses')
    response = session.get(f'https://akademik.itb.ac.id/app/mahasiswa:{nim}/kelas')
    response = session.get(response.url)
    parsed_html = BeautifulSoup(response.text, features='html.parser')

    # get current schedule
    # selector: td with bg-info class
    current_schedule = parsed_html.body.find('td', attrs={'class': 'bg-info'})
    
    # check if weekend
    if current_schedule is None:
        print('[INFO] this is weekend, no class :)')
        return []
    # parse all course
    divs = current_schedule.find_all('div')
    courses = []
    for div in divs:
        if div.has_attr('title'):
            title = div.a['data-kuliah']
            url = div.a['data-url']
            courses.append({
                'title': title,
                'url': url
            })
    
    return courses

def check_course(session, course):
    response = session.get(f'https://akademik.itb.ac.id{course["url"]}')
    parsed_html = BeautifulSoup(response.text, features='html.parser')
    time = parsed_html.dl.find_all('dd')[0].decode_contents().strip()
    lecturer = parsed_html.dl.find_all('dd')[1].decode_contents().strip()
    
    print('Course detail')
    print('course:', course['title'])
    print('lecturer:', lecturer)
    print('time:', time)

    # check if class attendance has been set
    if parsed_html.find('strong'):
        print('Class attendance set at:', parsed_html.find('strong').decode_contents().strip())
    else:
        print('Class attendance is not set')
