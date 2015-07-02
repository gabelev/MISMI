

def url_builder(page_range, terms):
    base_url = 'http://www.amazon.com/s/rh=%2Ck%3A'
    page = '&page='
    plus = '+'
    search_terms = plus.join(terms.split())
    return [base_url + search_terms + page + str(i) for i in range(1, page_range)]


