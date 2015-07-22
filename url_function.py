from keyword_list import terms_list

class Url_builder(object):

    @staticmethod
    def url_builder(page_range, terms):
        base_url = 'http://www.amazon.com/s/rh=%2Ck%3A'
        page = '&page='
        plus = '+'
        search_terms = plus.join(terms.split())
        return [base_url + search_terms + page + str(i) for i in range(1, page_range+1)]
    
    @staticmethod
    def url_builder_books(page_range, terms):
        base_url = 'http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Dstripbooks&field-keywords='
        page = '&page='
        plus = '+'
        search_terms = plus.join(terms.split())
        return [base_url + search_terms + page + str(i) for i in range(1, page_range+1)]
    
    @staticmethod
    def url_builder_kindle(page_range, terms):
        base_url = 'http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Ddigital-text&field-keywords='
        page = '&page='
        plus = '+'
        search_terms = plus.join(terms.split())
        return [base_url + search_terms + page + str(i) for i in range(1, page_range+1)]

    @classmethod
    def url_dict_builder(self, page_range, list_of_terms):
        set_of_terms = set(list_of_terms)
        result = {}
        for term in set_of_terms:
            urls_term = (term, 'all')
            urls = self.url_builder(page_range, term)
            result[urls_term] = urls
        for term in set_of_terms:
            urls_term = (term, 'books')
            urls = self.url_builder_books(page_range, term)
            result[urls_term] = urls
        for term in set_of_terms:
            urls_term = (term, 'Kindle')
            urls = self.url_builder_kindle(page_range, term)
            result[urls_term] = urls
        return result
    
	# @classmethod
	# def url_dict_builder(self, page_range, list_of_terms):
	#     set_of_terms = set(list_of_terms)
	#     result = {}
	#     for term in set_of_terms:
	#         urls_term = {}
	#         urls = self.url_builder(page_range, term)
	#         result[term] = urls
	#     return result