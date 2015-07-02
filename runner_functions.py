from tracker_functions import Tracker
from reformat_functions import Reformat
from endpoints import Search_all
from asins import business_search_asins, business_tracking, amish_asin, all_search_asins, all_tracking

class Runner(object):

	@classmethod
	def all_search_runner(self):
	    print("----MSG: Running All Search")
	    all_search_result = Tracker.run_spider_run(Search_all, all_search_asins)
	    reformat.make_pickle(all_search_result, "all_search")
	    reformat.reformat_data_add_column(all_search_result, 'all_search', 'search', all_tracking, collection_all_search)

	@classmethod
	def business_search_runner():
	    print("----MSG: Running Business Search")
	    business_result = run_spider_run(Search_Business, business_search_asins)
	    make_pickle(business_result, "business_search")
	    reformat_data_add_column(business_result, 'business_search', 'search', business_tracking, collection_business_search)

	@classmethod
	def amish_search_runner():
	    print("----MSG: Running Amish Search")
	    amish_search_result = run_spider_run(Search_Amish, amish_asin)
	    make_pickle(amish_search_result, "amish_search")
	    reformat_data_add_column(amish_search_result, 'amish_search', 'search', amish_asin, collection_amish_search)

	@classmethod
	def amish_category_runner():
	    print("----MSG: Running Amish Category")
	    amish_category_result = run_spider_run(Category_Amish, amish_asin)
	    make_pickle(amish_category_result, "amish_category")
	    reformat_data_add_column(amish_category_result, 'amish_category', 'category', amish_asin, collection_amish_category)    

	@classmethod
	def amish_bestseller_runner():
	    print("----MSG: Running Amish Bestseller")
	    amish_bestseller_result = run_spider_bestseller(Best_Amish, amish_asin)
	    make_pickle(amish_bestseller_result, "amish_best")
	    reformat_data_add_column_bestseller(amish_bestseller_result, 'amish_bestseller', 'bestseller', amish_asin, collection_amish_bestseller)

	@classmethod
	def all_runner():
	    print("----MSG: Running All")
	    business_result = run_spider_run(Search_Business, business_search_asins)
	    make_pickle(business_result, "business_search")
	    reformat_data_add_column(business_result, 'business_search', 'search', business_tracking, collection_business_search)

	    amish_category_result = run_spider_run(Category_Amish, amish_asin)
	    make_pickle(amish_category_result, "amish_category")
	    reformat_data_add_column(amish_category_result, 'amish_category', 'category', amish_asin, collection_amish_category)

	    amish_search_result = run_spider_run(Search_Amish, amish_asin)
	    make_pickle(amish_search_result, "amish_search")
	    reformat_data_add_column(amish_search_result, 'amish_search', 'search', amish_asin, collection_amish_search)

	    amish_bestseller_result = run_spider_bestseller(Best_Amish, amish_asin)
	    make_pickle(amish_bestseller_result, "amish_best")
	    reformat_data_add_column_bestseller(amish_bestseller_result, 'amish_bestseller', 'bestseller', amish_asin, collection_amish_bestseller)