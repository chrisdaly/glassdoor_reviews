Glassdoor Reviews
--------

Basic usage::
	
    >>> from glassdoor_reviews import ReviewPage
    >>> import requests
    >>>
    >>> data = []
    >>> url = "https://www.glassdoor.co.uk/Reviews/Aetna-Reviews-E16.htm"
    >>> headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36"}
    >>> params = {"filter.defaultEmploymentStatuses": False, "filter.defaultLocation": False}
    >>> response = requests.get(url, params=params, headers=headers)
    >>> 
    >>> print(response.url)
    >>> rp = ReviewPage.from_response(response)
    >>>
    >>> data = []
	>>> for review in rp.reviews():
    >>> 	data.append(review)
    >>>
    >>> url = rp.next_page_url