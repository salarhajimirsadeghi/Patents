"""
This script is converting XML files to JSON
"""

import os 
from xml2json import xml2json



directory = "/Users/Salar_Hajimirsadeghi/Google Drive/Projects/Patents/Data/l20170131/I20170131"



for folder in os.listdir(directory):	
	# Directory: ".../I20170131/UTIL____"
	if (folder.startswith('UTIL')):			
		new_directory = directory + "/"+ folder

		# Now going through all the files that we unzipped
		for uz_folder in os.listdir(new_directory):			
			try:
				final_dir = new_directory + "/" + uz_folder
				os.chdir(final_dir)				
				for files in os.listdir(final_dir):
					if(files.lower().endswith(('.xml'))): 								
						command = "xml2json < " + files + " > " + files[:-4] + ".json"
						os.system(command)
			except:
				continue

					