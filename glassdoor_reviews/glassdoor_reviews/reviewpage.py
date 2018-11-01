from bs4 import BeautifulSoup as BS
from .review import Review

class ReviewPage(object):
    def __init__(self, soup):
        self.soup = soup

    @property
    def review_containers(self):
        return self.soup.find_all('li', ' empReview cf ')

    @property
    def next_page_url(self):
        atag = self.soup.find('li', 'next').find('a')
        if atag is not None:
            return 'https://www.glassdoor.co.uk' + atag['href']

    def reviews(self):
        for rc in self.review_containers:
            yield Review(rc).parse()

    @classmethod
    def from_response(cls, response):
        soup = BS(response.text, 'lxml')
        return cls(soup)

    @classmethod
    def from_html(cls, html):
        soup = BS(html, 'lxml')
        return cls(soup)