# Glassdoor Reviews
Extracts all reviews on a given company's glassdoor page.

## Example
```
import time
import requests

from glassdoor_reviews import ReviewPage

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile \
     Safari/537.36'
}

params = {
    "filter.defaultEmploymentStatuses": False, 
    "filter.defaultLocation": False    
}

start_url = 'https://www.glassdoor.co.uk/Reviews/Vertex-Pharmaceuticals-Reviews-E2080.htm'
url = start_url
data = []

while True:
    if not url:
        break
    time.sleep(1)
    r = requests.get(url, headers=headers, params=params)
    print(r.url)
    rp = ReviewPage.from_response(r)
    for review in rp.reviews():
        data.append(review)
    url = rp.next_page_url
```
