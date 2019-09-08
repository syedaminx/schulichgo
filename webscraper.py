from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import requests
import psycopg2
import config

#opening up browser
headers = {'User-Agent': 'Chrome/65.0'}
driver = webdriver.Chrome()

def template():
    #opening up york website
    driver.get('https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm')

    #attempting to click on "Advanced Search" to search courses by on the york website
    try:
        elem = driver.find_element_by_xpath('/html/body/p/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/ul/li[1]/ul/li[9]/a');
        if elem.is_displayed():
            elem.click() # this will click the element if it is there
    except NoSuchElementException:
        print("...")
        advanced_search = driver.find_element_by_xpath('/html/body/p/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/ul/li[1]/ul/li[9]/a').click();

    #choosing Schulich as the faculty
    faculty = Select(driver.find_element_by_name('facultyPopup'));
    faculty.select_by_visible_text("Schulich School of Business - (SB)");

    #pausing for 1 second to allow for update of subjects
    time.sleep(1)

    #choosing the current academic year as the session
    session = Select(driver.find_element_by_name('sessionPopup'));
    session.select_by_visible_text("Fall/Winter 2018-2019")

course_data_arr = []

def preselect():
    #going to advanced search url
    driver.get(search_url)

    #choosing Schulich as the faculty
    faculty = Select(driver.find_element_by_name('facultyPopup'));
    faculty.select_by_visible_text("Schulich School of Business - (SB)");

    #pausing for 1 second to allow for update of subjects
    time.sleep(1)

    #choosing the current academic year as the session
    session = Select(driver.find_element_by_name('sessionPopup'));
    session.select_by_visible_text("Fall/Winter 2018-2019")

def get_course_info():
    url = driver.current_url
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    course = soup.find_all('p')
    course_code = course[0].text[3:][:9]
    course_cat = course[0].text[3:][:4]
    course_num = int(course[0].text[8:][:4])
    course_name = course[0].text[22:]
    course_desc = course[3].text
    results = soup.findAll("td", {"valign": "TOP","width" : "15%"})[1::2]
    list_instruct = [x.text.replace('\xa0',' ') for x in results]
    list_instruct = filter(lambda name: name.strip(), list_instruct)
    final = list(set(list_instruct))
    time_created = datetime.now().strftime('%B, %d, %Y %I:%M %p')
    course_data = (course_code, course_cat, course_num, course_name, course_desc, final, time_created)
    course_data_arr.append(course_data)

def course_urls():
    link_click = driver.find_elements_by_link_text('Fall/Winter 2018-2019 Course Schedule')
    i = 0
    my_list = []
    for pages in link_click:
        course_url = link_click[i].get_attribute("href")
        my_list.append(course_url)
        i += 1

template()
subject = Select(driver.find_element_by_name('subjectPopup'));

sub_len = len(subject.options) - 1

x = 0
while x < sub_len:
    subject.select_by_index(x)
    driver.find_element_by_name('3.10.8.11.0').click()
    link_click = driver.find_elements_by_link_text('Fall/Winter 2018-2019 Course Schedule')
    i = 0
    my_list = []
    for pages in link_click:
        course_url = link_click[i].get_attribute("href")
        my_list.append(course_url)
        i += 1
    z = 0
    while z < len(my_list):
        driver.get(my_list[z])
        get_course_info()
        z += 1

    template()

    subject = Select(driver.find_element_by_name('subjectPopup'));

    x += 1

#connecting and inserting into database
conn = psycopg2.connect(host="localhost",database="schulichgo_development", user="", password="")
cursor = conn.cursor()
conn.rollback()
inserting = ("INSERT INTO courses (code, category, number, name, description, instructors, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s)")
cursor.executemany(inserting, course_data_arr)
conn.commit()
conn.close()
