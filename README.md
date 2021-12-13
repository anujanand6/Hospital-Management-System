# Hospital Management System
This repository serves as the final project for the course CS 5200 Database Management Systems.

## How To Run
1) Clone this repository
2) Install the required packages using the command: ```pip install -r requirements.txt```
3) Open a MySQL connection
4) Import the contents of the folder ```HMS_DB_DUMP``` to MySQL
   1) Click on ```Server``` -> ```Data Import```
   2) Choose ```Import from Dump Project Folder```
   3) Choose directory where the folder is located
   4) Click on ```Load Folder Contents```
   5) Select the ```db_project``` schema
   6) Click on ```Start Import```
   7) Verify that the required tables have been imported
5) Modify the variables ```USER```, ```PASSWORD``` and ```DB_SCHEMA``` in the ```database.py```
6) Open a terminal window and navigate to the project directory
7) Run the command:``` streamlit run app.py ```
8) The streamlit webpage should be accessible from the browser on this URL: ```http://localhost:8501/```
