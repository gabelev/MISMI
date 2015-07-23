__author__ = 'glevine@penguinrandomhouse.com'
__version__ = 'MISMI 0.3'

from bs4 import BeautifulSoup
import urllib2


import time
import lxml
import csv
import requests
import re
import sys
import os


from retry import retry as _retry
from tracker_functions import Tracker
from reformat_functions import Reformat
from runner_functions import Runner

# from endpoints import Search_all
from asins import business_search_asins, business_tracking, amish_asin, all_search_asins, all_tracking

reload(sys)
sys.setdefaultencoding("utf-8")

# def url_builder(page_range, terms):
#     base_url = 'http://www.amazon.com/s/rh=%2Ck%3A'
#     page = '&page='
#     plus = '+'
#     search_terms = plus.join(terms.split())
#     return [base_url + search_terms + page + str(i) for i in range(1, page_range)]







if __name__ == "__main__":

    home_msg = "----- MISMI: AMAZON TRACKING TOOL \n---- by G.Levine"
    db_msg = "----- MSG: ACTIVATE DATABASE - MongoDB"
    last_msg = "----- AMAZON TRACKING Complete. Have a nice day."

    print(home_msg)



    print(db_msg)
    print("Would you like to run the tracker? Yes")
    # print("Which tracker would you like to run?")
    # print("All, All Search, Business Search, All Amish, Amish Search, Amish Category, Amish Bestseller?")
    action = raw_input("> ")
    if action == "Yes":
        run = Runner()
        run.all_search_runner()
    # if action == "All":
    #     runner.all_runner()
    # if action == "All Search":
    #     run = Runner()
    #     run.all_search_runner()
    # if action == "Business Search":
    #     runner.business_search_runner()
    # if action == "Amish Search":
    #     runner.amish_search_runner()
    # if action == "Amish Category":
    #     runner.amish_category_runner()
    # if action == "Amish Bestseller":
    #     runner.amish_bestseller_runner()
    # if action == "All Amish":
    #     print("Running through all Amish")
    #     runner.amish_category_runner()
    #     runner.amish_search_runner()
    #     runner.amish_bestseller_runner()
    # else:
    #     print("please input again")

    print(last_msg)