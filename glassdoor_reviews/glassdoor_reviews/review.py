class Review(object):
    def __init__(self, soup):
        self.soup = soup

    def _parse_variable_name(self, name):
        return name.lower().replace('&', 'and').replace(' ', '_').replace('/', '_')
    
    def _parse_row(self, row):
        key_div = row.find('div')
        value_span = row.find('span')
        if (key_div is not None) and (value_span is not None):
            key = self._parse_variable_name(key_div.get_text())
            value = value_span.get('title')
            return {key: value}
    
    @property
    def review_id(self):
        return self.soup['id'].split('_')[1]

    @property
    def title(self):
        titlebar = self.soup.find('a', class_='reviewLink')
        if titlebar is not None:
            return titlebar.get_text().strip('"')

    @property
    def position(self):
        author_span = self.soup.find('span', class_='authorJobTitle middle reviewer')
        if author_span is not None:
            return author_span.get_text().strip('"')

    @property
    def location(self):
        location_span = self.soup.find('span', class_='authorLocation middle')
        if location_span is not None:
            return location_span.get_text().strip('"')

    @property
    def date(self):
        date_span = self.soup.find('time')
        if date_span is not None:
            return date_span.get('datetime')

    @property
    def sub_ratings(self):
        ratings = {}
        rating_table = self.soup.find('ul', 'undecorated')
        if rating_table is not None:
            rows = rating_table.findAll('li')
            if rows is not None:
                for row in rows:
                    ratings.update(self._parse_row(row))
                return ratings

    @property
    def recommendations(self):
        spans = self.soup.find_all('span')
        recs = {}
        for span in spans:
            text = span.get_text()
            if 'Recommend' in text:
                recs['recommends'] = text
            elif 'Outlook' in text:
                recs['outlook'] = text
            elif 'CEO' in text:
                recs['approval_of_ceo'] = text
        return recs

    @property
    def overall_rating(self):
        rating = self.soup.find('span', class_='value-title')
        if rating is not None:
            return rating.get('title')
    
    @property
    def pros(self):
        pros = self.soup.find('p', class_='pros')
        if pros is not None:
            return pros.get_text().strip('"')

    @property
    def cons(self):
        cons = self.soup.find('p', class_='cons')
        if cons is not None:
            return cons.get_text().strip('"')
        
    @property
    def advice(self):
        advice = self.soup.find('p', class_='adviceMgmt')
        if advice is not None:
            return advice.get_text().strip('"')

    @property
    def link(self):
        link = self.soup.find('a', class_='reviewLink')
        if link is not None:
            return 'https://www.glassdoor.com' + link.get('href')   

    def parse(self):
        data = {
            'id': self.review_id,
            'title': self.title,
            'position': self.position,
            'location': self.location,
            'date': self.date,
            'pros': self.pros,
            'cons': self.cons,
            'advice': self.advice,
            'link': self.link,
            'rating': self.overall_rating,
        }

        sub_ratings = self.sub_ratings
        if sub_ratings is not None:
            data.update(sub_ratings)

        recommendations = self.recommendations
        if recommendations is not None:
            data.update(recommendations)
            
        return data
