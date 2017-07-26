## Overview:
 - Retrieve Patent information by parsing through the API

## Project Description:
 - This Project was created to retrieve necessary Patent information for the entire month of January.
 - The Patent informations that have been stored are Patent Number, Title, and Description
 - It includes files that complete the following tasks:
   - Create a MySQL table (Table_Creation.sql)
   - Unzipping all files (unzipping_script.py)
   - Convert from XML to JSON (json2db_script.py)
   - Move all JSON files to shared location (move_json.py)
   - Input data into Databse (data_in_DB_script.py)

## Setup and Usage:
  - Each python file has been created for a certain task thus it can be applied to all patents
  - The task of each task is mentioned above along with their respected order
  
## Improvements:
 - Utilize ec2 instance
 - shave off some aspects of json files so you're not worrying about them since only a small portion is useful to us.
 - Databse has been created for more information than inputted, so retrieve other patent information
