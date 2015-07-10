from bs4 import BeautifulSoup
import urllib2
import lxml
import lxml.etree
import datetime
import requests
import re
import urllib2
import time

from retry import retry as _retry
# from endpoints import Search_all
from asins import business_search_asins, business_tracking, amish_asin, all_search_asins, all_tracking


class Tracker(object):

	@staticmethod
	def iter_elements_extract_or_skip_attributes(elements, *attributes):
	    for element in elements:
	        values = tuple(element.get(att, None) for att in attributes)
	        if all(values):
	            yield values

	@staticmethod
	def check_asin(result_list, isbn_set):
	    new_result = [item for item in result_list if item[1] in isbn_set]
	    return new_result

	@staticmethod
	def remove_prefix(s, prefix):
	    assert s.startswith(prefix)
	    return s[len(prefix):]

	@staticmethod
	def convert_index(result_list):
	    getidx = lambda s: 1 + int(Tracker.remove_prefix(s, 'result_'))
	    return [(getidx(s), asin) for s, asin in result_list]

	@staticmethod
	@_retry(urllib2.URLError, tries=4, delay=3, backoff=2)
	def urlopen_with_retry(url):
	    return urllib2.urlopen(url)

	@staticmethod
	def Amz_Search_Results(endpoint, isbn_set):
	    amz = Tracker.urlopen_with_retry(endpoint)
	    soup = BeautifulSoup(amz, "lxml")
	    findone = BeautifulSoup(str(soup.find_all("li", class_="s-result-item")))
	    elements = findone.find_all('li')
	    iter_data = Tracker.iter_elements_extract_or_skip_attributes(elements, 'id', 'data-asin')
	    return [item for item in iter_data if item[1] in isbn_set]

	@staticmethod
	def Amz_Search_Results_alt(endpoint, isbn_set):
	    amz = Tracker.urlopen_with_retry(endpoint)
	    soup = BeautifulSoup(amz, "lxml")
	    findone = BeautifulSoup(str(soup.find_all("div", attrs={"id": "mainResults"})))
	    elements = findone.find_all('div')
	    iter_data = Tracker.iter_elements_extract_or_skip_attributes(elements, 'id', 'name')
	    return [item for item in iter_data if item[1] in isbn_set]

	@staticmethod
	def Amz_bestseller(endpoint, isbn_set):
	    r = requests.get(endpoint)
	    soup = BeautifulSoup(str(r.text), "html")
	    findtwo = BeautifulSoup(str(soup.find_all("div", attrs={"class": "zg_itemImmersion"})))
	    rank = BeautifulSoup(str(findtwo.find_all("span", attrs={"class": "zg_rankNumber"})))
	    find_rank = rank.text
	    rank_list = map(int, re.findall('\d+', find_rank))
	    title_list = []
	    for tag in findtwo.find_all('img'):
	        title_list.append(tag.get('title'))
	    asin_list = []
	    for b in findtwo.find_all("span", attrs={"class": "asinReviewsSummary acr-popover"}):
	        x = b['name']
	        asin_list.append(x)
	    final_result = check_asin(zip(rank_list, asin_list, title_list), isbn_set)
	    return final_result

	@classmethod
	def run_spider_run(self, item_search, isbn_set):
	    self.results_dict = {}
	    for key, value in item_search.iteritems():
	        results = []
	        for url in value:
	            # try:
	            time.sleep(0.5)
	            x = self.Amz_Search_Results(url, isbn_set)
	            if x == []:
	                time.sleep(0.5)
	                x = self.Amz_Search_Results_alt(url, isbn_set)
	            results.extend(Tracker.convert_index(x))
	            self.results_dict[key] = results
	    return self.results_dict

	@classmethod
	def run_spider_bestseller(self, item_search, isbn_set):
	    self.results_dict = {}
	    for key, value in item_search.iteritems():
	        results = []
	        for url in value:
	            time.sleep(0.5)
	            x = self.Amz_bestseller(url, isbn_set)
	            results.extend(x)
	            self.results_dict[key] = results
	    return self.results_dict