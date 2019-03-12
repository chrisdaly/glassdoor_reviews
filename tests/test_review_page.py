import unittest
import requests
from bs4 import BeautifulSoup as BS
from glassdoor_reviews import Review, ReviewPage


class TestStaticReviewPage(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        file_path = "./tests/glassdoor_reviews_test.html"
        with open(file_path, "r", encoding='utf-8') as f:
            html = f.read()
        self.review_page = ReviewPage.from_html(html)

    def test_review_containers(self):
        reviews = self.review_page.review_containers
        expected = 10
        self.assertEqual(10, len(reviews))

    def test_next_page(self):
        expected_next_page = "https://www.glassdoor.co.uk/Reviews/Aetna-Reviews-E16_P234.htm?filter.defaultEmploymentStatuses=false&filter.defaultLocation=false"
        self.assertEqual(expected_next_page, self.review_page.next_page_url)

    def test_review_parsing(self):
        expected_data = {
            "id": "12449",
            "title": "Good but needs improvement",
            "position": "Current Employee - Senior Consultant",
            "location": "Philadelphia, PA (US)",
            "date": "2008-06-12",
            'helpful': '2',
            "pros": "401k and relatively good job security",
            "cons": "Outsourcing!! High cost of benefits. Budget restrictions to help 'save' the company money.",
            "advice": "Take care of your employees! Share the wealth.",
            "link": "https://www.glassdoor.co.uk/Reviews/Employee-Review-Aetna-RVW12449.htm",
            "rating": "3.0",
            "css_class": " empReview cf toggleable ",
            "sub_ratings": {
                "work_life_balance": "3.5",
                "career_opportunities": "3.0",
                "comp_and_benefits": "2.0",
                "senior_management": "3.0"
            },
            "recommendations": {
                "approval_of_ceo": "Approves of CEO"
            }
        }

        parsed_data = list(self.review_page.reviews())[0]
        self.assertDictEqual(expected_data, parsed_data)


class TestLiveReviewPage(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        url = "https://www.glassdoor.co.uk/Reviews/Employee-Review-Vertex-Pharmaceuticals-RVW24494015.htm"
        headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36"}
        params = {"filter.defaultEmploymentStatuses": False, "filter.defaultLocation": False}
        response = requests.get(url, headers=headers, params=params)
        assert response.ok
        soup = BS(response.text, "lxml")
        # When you specify a review id in the URL, the review appears it its own div, not in an OL.
        review = soup.find("div", class_="empReview")
        self.review = Review(review)

    def test_review_parsing(self):
        expected_data = {
            'css_class': 'pad empReview cf ',
            'advice': 'get lost',
            'cons': 'selfindulged executives that act as if they care but pocket '
            'millions. Scientists are frantically searching for new leads as CSO '
            'comes up with nothing but nonsense.',
            'date': '2019-02-01',
            'helpful': None,
            'id': '24494015',
            'link': None,
            'location': 'Abingdon, England',
            'position': 'Former Employee - Anonymous Employee',
            'pros': 'great science, dedicated workforce and good salaries/stock options',
            'rating': '3.0',
            'recommendations': {
                'approval_of_ceo': 'Disapproves of CEO',
                'outlook': 'Positive Outlook'
            },
            'sub_ratings': {
                'comp_and_benefits': '5.0',
                'culture_and_values': '3.0',
                'senior_management': '1.0',
                'work_life_balance': '3.0'
            },
            'title': None
        }

        parsed_data = self.review.parse()
        # Reviews can be updated (e.g. a new person clicks the "helpful" button), => only compare non-metric fields.
        parsed_data["helpful"] = None
        self.assertDictEqual(expected_data, parsed_data)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    test_classes_to_run = [TestStaticReviewPage, TestLiveReviewPage]

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)
    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
