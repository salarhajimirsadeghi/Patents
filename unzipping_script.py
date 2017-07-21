"""
This script 
"""


import os

directory = "/Users/Salar_Hajimirsadeghi/Google Drive/Projects/Patents/Data"


for folder in os.listdir(directory):	
	if (folder.startswith('l')):			

		# Directory: ".../Data/l20170131/"
		directory2 = directory +"/" +folder		
		
		for folder2 in os.listdir(directory2):			

			# Directory: ".../Data/l20170131/I20170131"
			if (folder2[1:] == folder[1:]):
				directory3 = directory2 + "/" + folder2			

				for folder3 in os.listdir(directory3):

					# Directory: ".../Data/l20170131/I20170131/UTIL____"
					if(folder3.startswith('UTIL')):
						last_directory = directory3 + "/" + folder3						
						for f in os.listdir(last_directory):
							os.system('unzip "*.zip"')



