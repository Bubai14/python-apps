import time

import requests
import selectorlib
import db

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}


class WebScrapper:
    def scrape(self, url):
        """
        Scrape the page source from the URL
        :param url:
            The url to be scrapped
        :return:
            the scrapped page source
        """
        response = requests.get(url, headers=HEADERS)
        page_source = response.text
        return page_source

    def extract(self, page_source):
        """
        Extracts the contents from the source
        :param page_source:
            The page source
        :return:
            The extracted content
        """
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        return extractor.extract(page_source)['tours']


class Data:
    def store(self, extracted):
        """
        Store the extracted value to the database
        :param extracted:
            extracted value
        :return:
        """
        database = db.Database('data.db')
        row = extracted.split(',')
        row = [item.strip() for item in row]
        database.save(row)

    def read(self, extracted):
        """
        Read the values from database
        :return:
            the tours list
        """
        database = db.Database('data.db')
        row = extracted.split(',')
        row = [item.strip() for item in row]
        return database.get(row)


def message():
    print("Done!!!")


if __name__ == "__main__":
    web_scrapper = WebScrapper()
    data = Data()
    while True:
        source = web_scrapper.scrape(URL)
        extracted = web_scrapper.extract(source)
        if extracted != "No upcoming tours":
            content = data.read(extracted)
            if not content:
                data.store(extracted)
                message()
        time.sleep(2)
