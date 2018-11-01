import time
import requests

from glassdoor_reviews import ReviewPage

def test_parse_review_page():
	headers = {
	    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
	     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile \
	     Safari/537.36'
	}

	params = {
	    "filter.defaultEmploymentStatuses": False, 
	    "filter.defaultLocation": False    
	}

	url = 'https://www.glassdoor.co.uk/Reviews/Vertex-Pharmaceuticals-Reviews-E2080.htm'		# 
	r = requests.get(url, headers=headers, params=params)
	rp = ReviewPage.from_response(r)
	assert rp.next_page_url == 'https://www.glassdoor.co.uk/Reviews/Vertex-Pharmaceuticals-Reviews-E2080_P2.htm?filter.defaultEmploymentStatuses=false&filter.defaultLocation=false'
	
if __name__ == '__main__':
	test_parse_review_page()
	print('passed')