from keyword_list import terms_list

class Url_builder(object):

	@staticmethod
	def url_builder(page_range, terms):
	    base_url = 'http://www.amazon.com/s/rh=%2Ck%3A'
	    page = '&page='
	    plus = '+'
	    search_terms = plus.join(terms.split())
	    return [base_url + search_terms + page + str(i) for i in range(1, page_range+1)]


	@classmethod
	def url_dict_builder(self, page_range, list_of_terms):
	    set_of_terms = set(list_of_terms)
	    result = {}
	    for term in set_of_terms:
	        urls_term = {}
	        urls = url_builder(page_range, term)
	        result[term] = urls
	    yield result