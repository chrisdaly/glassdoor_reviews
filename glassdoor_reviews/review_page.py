from bs4 import BeautifulSoup as BS
from .review import Review


class ReviewPage(object):
    def __init__(self, soup):
        self.soup = soup

    @property
    def review_containers(self):
        review_feed = self.soup.find("ol", class_="empReviews")
        if review_feed is not None:
            review_containers = review_feed.findChildren("li", recursive=False)
            return review_containers

    @property
    def next_page_url(self):
        atag = self.soup.find("li", class_=lambda x: "next" in x if x else None)
        if (atag is not None) and atag.a:
            return 'https://www.glassdoor.co.uk{}'.format(atag.a["href"])

    def reviews(self):
        for rc in self.review_containers:
            yield Review(rc).parse()

    @classmethod
    def from_response(cls, response):
        soup = BS(response.text, "lxml")
        return cls(soup)

    @classmethod
    def from_html(cls, html):
        soup = BS(html, "lxml")
        return cls(soup)


if __name__ == '__main__':
    url = "https://www.glassdoor.co.uk/Reviews/Aetna-Reviews-E16_P234.htm?filter.defaultEmploymentStatuses=false&filter.defaultLocation=false"
