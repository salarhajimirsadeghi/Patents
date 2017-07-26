"""
This script will get the Necessary info 
From the json file and upload it to the DB


Step1:
Load json file

Step2: 
Iterate through JSON Object

Step3:
Dump right info into DB

"""

import json
from pprint import pprint
import mysql.connector
 

############ Database Information ######### 
HOST = "localhost"
USER = "root"
PASSWD = "012394"
DATABASE = "Patents"
 
cnx = mysql.connector.connect(host=HOST, user=USER, passwd=PASSWD, database=DATABASE)
cursor = cnx.cursor()

############ Storing API data into MYSQL ############
def store_data(Patent_ID, Title, Description):
    
	try:
	    insert_query = ("INSERT INTO Patents (ID, Title, Description) VALUES \
										(%s, %s, %s)")
	    cursor.execute(insert_query, (Patent_ID, Title, Description))

	    cnx.commit()
	    return
	
	except:
		return
#########################################################


################## Global Variables #####################
title = ""
desc = ""
Patent_ID = ""
#########################################################

""" Loading json files """
file_directory = "/Users/Salar_Hajimirsadeghi/Google Drive/Projects/Patents/Data/l20170131/I20170131/UTIL09554/US09554496-20170131/US09554496-20170131.json"
with open(file_directory) as data_file:    
    json_data = json.load(data_file)

json_data = json_data['us-patent-grant']

#Going Through the file's JSON OBJECT
for item in json_data:
	try:
		#Grabs Title
		if (item == "us-bibliographic-data-grant"):
			json_title = json_data[item]
			for element in json_title:
				if(element == "invention-title"):
					title = json_title[element]["$t"]
					# print(title)

				#Grabs Patent ID
				if(element == "publication-reference"):
					json_id = json_title[element]
					
					for docId in json_id:												
						if(docId == "document-id"):
							json_id = json_id[docId]
							for pNumber in json_id:						
								if (pNumber == "doc-number"):
									Patent_ID = "US" + json_id[pNumber]["$t"]									

		#Grabs the Description
		if(item == "description"):
			json_description = json_data[item]
			for p in json_description:
				if (p == "p"):
					desc = ""	
					# print(json_description[p])
					for num in json_description[p]:						
						desc += " " + ''.join(num["$t"])																					
					# print(brief_desc)
		
	except:
		#if it doesn't exist, just continue
		continue

store_data(Patent_ID, title, desc)



