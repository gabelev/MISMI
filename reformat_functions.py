import datetime
import pickle
import pandas as pd
import csv

class Reformat(object):

	@classmethod
	def reformat_data_add_column(self, data_name, output_name, rank_type, tracking_asin, database_collection):
	    df = pd.DataFrame.from_dict(data_name, orient='index')
	    data = df.transpose()
	    results = []
	    today = str(datetime.datetime.now())
	    for index, row in data.iteritems():
	        for old_cell in row:
	            if pd.notnull(old_cell):
	                cell = str(old_cell)
	                cell = cell.split(',')
	                rank = cell[0][1:]
	                number = cell[1][2:-2]
	                tracking = 'no'
	                if number in tracking_asin:
	                    tracking = 'yes'
	                x = index, rank, number, rank_type, today, tracking
	                results.append(x)
	    name = output_name + "_" + today.replace(" ", "_").replace(".", ":") + '.csv'
	    myfile = open(name, 'wb')
	    wr = csv.writer(myfile, delimiter=',', quoting= csv.QUOTE_ALL)
	    head = ('Terms', 'Rank', 'ASIN/ISBN', 'Rank Type', 'Date/time Collected', 'tracking')
	    wr.writerow(head)
	    for row in results:
	        wr.writerow(row)
	    print("----- MSG: CSV output")
	    dex = output_name+"_"+today[0:10]
	    results_d = {}
	    results_d[dex] = results
	    database_collection.insert(results_d)
	    print("----- MSG: DATABASE Write")
	    print("----- MSG: NEXT PROCESS STARTING")

	@classmethod
	def reformat_data_add_column_bestseller(self, data_name, output_name, rank_type, tracking_asin, database_collection):
	    df = pd.DataFrame.from_dict(data_name, orient='index')
	    data = df.transpose()
	    results = []
	    today = str(datetime.datetime.now())
	    for index, row in data.iteritems():
	        for old_cell in row:
	            if pd.notnull(old_cell):
	                cell = str(old_cell)
	                cell = cell.split(',')
	                rank = cell[0][1:]
	                number = cell[1][2:-1]
	                tracking = 'no'
	                if number in tracking_asin:
	                    tracking = 'yes'
	                x = index, rank, number, rank_type, today, tracking
	                results.append(x)
	    name = output_name + "_" + today.replace(" ", "_").replace(".", ":") + '.csv'
	    myfile = open(name, 'wb')
	    wr = csv.writer(myfile, delimiter=',', quoting= csv.QUOTE_ALL)
	    head = ('Terms', 'Rank', 'ASIN/ISBN', 'Rank Type', 'Date/time Collected', 'tracking')
	    wr.writerow(head)
	    for row in results:
	        wr.writerow(row)
	    print("----- MSG: CSV output")
	    dex = output_name+"_"+today[0:10]
	    results_d = {}
	    results_d[dex] = results
	    database_collection.insert(results_d)
	    print("----- MSG: DATABASE Write")
	    print("----- MSG: NEXT PROCESS STARTING")

	@classmethod
	def make_pickle(self, data_name, output_name):
	    today = str(datetime.datetime.now())[0:10]
	    name = output_name + today + ".p"
	    pickle.dump( data_name, open( name, "wb" ) )
	    print("----- MSG: python output")