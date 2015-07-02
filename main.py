__author__ = 'glevine@penguinrandomhouse.com'

from bs4 import BeautifulSoup
import urllib2
import csv
import pandas as pd
import time
import lxml
import datetime
import pickle
import requests
import re
import sys
import os
import pymongo

from retry import retry as _retry
from tracker_functions import Tracker
from reformat_functions import Reformat
from runner_functions import Runner

from endpoints import Search_all
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
    db_msg = "----- MSG: DATABASE ACTIVE - MongoDB"
    last_msg = "----- AMAZON TRACKING Complete. Have a nice day."

    print(home_msg)

    conn = pymongo.MongoClient()
    db = conn.amzdb
    collection_amish_bestseller = db.amish_bestseller
    collection_amish_category = db.amish_category
    collection_amish_search = db.amish_search
    collection_business_search = db.business_search
    collection_all_search = db.all_search

    print(db_msg)
    print("Which tracker would you like to run?")
    print("All, All Search, Business Search, All Amish, Amish Search, Amish Category, Amish Bestseller?")
    action = raw_input("> ")
    if action == "All":
        runner.all_runner()
    if action == "All Search":
        run = Runner()
        run.all_search_runner()
    if action == "Business Search":
        runner.business_search_runner()
    if action == "Amish Search":
        runner.amish_search_runner()
    if action == "Amish Category":
        runner.amish_category_runner()
    if action == "Amish Bestseller":
        runner.amish_bestseller_runner()
    if action == "All Amish":
        print("Running through all Amish")
        runner.amish_category_runner()
        runner.amish_search_runner()
        runner.amish_bestseller_runner()
    # else:
    #     print("please input again")

    print(last_msg)