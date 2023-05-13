import requests
import selectorlib

# import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}


def scape(url):
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


def extract(page_source):
    """
    Extracts the contents from the source
    :param page_source:
        The page source
    :return:
        The extracted content
    """
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    print(extractor.extract(page_source))


if __name__ == "__main__":
    source = scape(URL)
    extract(source)

