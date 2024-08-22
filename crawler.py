from markdownify import MarkdownConverter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

webdriver_path = '/usr/lib/chromium-browser/chromedriver'
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)


def fetch_page(page_number):
    # make 5 static url for 5 first page of mentioned website

    url = ('https://qavanin.ir/?CAPTION=&Zone=&IsTitleSearch=true&IsTitleSearch=false'
           '&IsTextSearch=false&_isLaw=false&_isRegulation=false&_IsVote=false&_isOpenion=false'
           '&SeachTextType=3&fromApproveDate=&APPROVEDATE=&IsTitleSubject=False&IsMain=&COMMANDNO'
           '=&fromCommandDate=&COMMANDDATE=&NEWSPAPERNO=&fromNewspaperDate=&NEWSPAPERDATE'
           f'=&SortColumn=APPROVEDATE&SortDesc=True&Report_ID=&PageNumber={page_number}&page={page_number}&size=25&txtZone'
           '=&txtSubjects=&txtExecutors=&txtApprovers=&txtLawStatus=&txtLawTypes=')

    driver.get(url)

    time.sleep(15)

    return driver.page_source


def extract_data(page_source):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(page_source, 'html.parser')
    data_list = []

    law_items = soup.find_all('td', class_='text-justify')

    for item in law_items:
        title = item.find('a').text.strip()

        data_list.append({
            'title': title
        })

    return data_list


def save_to_markdown(data, file_name='laws_data.md'):
    with open(file_name, 'a', encoding='utf-8') as f:
        for entry in data:
            f.write(f"### {entry['title']}\n")


def scrape_qavanin():
    for number in range(1, 6):
        page_data = fetch_page(number)
        rendered_data = extract_data(page_data)
        save_to_markdown(rendered_data)


scrape_qavanin()
driver.quit()
