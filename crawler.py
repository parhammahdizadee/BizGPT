from markdownify import MarkdownConverter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from dotenv import dotenv_values

webdriver_path = dotenv_values(".env").get("WEBDRIVER_PATH")
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)


class Crawler:
    # TODO: can be convert to dynamic input of url

    @staticmethod
    def fetch_page(page_number):
        """
        make 5 static url for 5 page of mentioned website

        :param page_number: int

        :return: str: html of target page
        """

        url = ('https://qavanin.ir/?CAPTION=&Zone=&IsTitleSearch=true&IsTitleSearch=false'
               '&IsTextSearch=false&_isLaw=false&_isRegulation=false&_IsVote=false&_isOpenion=false'
               '&SeachTextType=3&fromApproveDate=&APPROVEDATE=&IsTitleSubject=False&IsMain=&COMMANDNO'
               '=&fromCommandDate=&COMMANDDATE=&NEWSPAPERNO=&fromNewspaperDate=&NEWSPAPERDATE'
               f'=&SortColumn=APPROVEDATE&SortDesc=True&Report_ID=&PageNumber={page_number}&page={page_number}&size=25&txtZone'
               '=&txtSubjects=&txtExecutors=&txtApprovers=&txtLawStatus=&txtLawTypes=')

        driver.get(url)

        time.sleep(15)

        return driver.page_source


class DataExtractor:
    """
    extract data from html
    """

    @staticmethod
    def extract_data(page_source):
        """
        :param page_source: html of target page
        :return: python list of data extracted from html
        """
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


class FormatConvertor:
    """
    save input data to a file format markdown
    """
    @staticmethod
    def save_to_markdown(data, file_name):
        with open(file_name, 'a', encoding='utf-8') as f:
            for entry in data:
                f.write(f"{entry['title']}-")


def scrape_qavanin():
    for number in range(1, 6):
        page_data = Crawler().fetch_page(number)
        rendered_data = DataExtractor().extract_data(page_data)
        FormatConvertor().save_to_markdown(rendered_data, 'laws_data.md')


scrape_qavanin()
driver.quit()
