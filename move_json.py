"""
This script moves all .json files to one location
"""

import os 
from shutil import copy2



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
					if(files.lower().endswith(('.json'))): 	
						copy2(files, "/Users/Salar_Hajimirsadeghi/Google Drive/Projects/Patents/Data/json_files")							
						# command = "cp " + files + "/Users/Salar_Hajimirsadeghi/Google Drive/Projects/Patents/Data/json_files/"
						# os.system(command)
			except:
				continue

					