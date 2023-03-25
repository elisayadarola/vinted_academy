
# I import the os so I can loop through it
import os
# I need to read the data in the CSV files first, so I import CSV for that matter. It's important that the database files are placed in the same folder as the code. 
import csv

def read_database(data):
    # I pass it an empty list that will receive all of the .csv data found in the loop.
    csv_files = []
    # for each file you find in the 'data' folder, list it.
    for file in os.listdir(data):
        # if the file is in csv format, open it and store the data with the name csvfile.
        if file.endswith('.csv'):
            with open(os.path.join(data, file), newline='') as csvfile:
                # store the csvfile data in the csv reader object. dictreader embedded function return an ordered dictionary for each row.
                reader = csv.DictReader(csvfile)
                # using the extend method to add the rows from each CSV file to the csv_file. If I used append instead of extend, because I want to add all the dictionaries to the list individually and not the entire reader object as one element.
                csv_files.extend(reader)
    # I get the list with the data already ordered by row. 
    return csv_files

clicks_csv = read_database('data/clicks')
users_csv = read_database('data/users')
all_user_data = clicks_csv + users_csv
# print(f"the count is: {clicks_csv.count(read_database('data/clicks'))}")
# print(all_user_data)

# here starts the mapping of the info. I will need two parameters for the map function, so the first will be the function obtaining two rows containig the date and the clicks info
def get_columns(row):
   try:
    return{"Date":row["date"], "Clicks":row["click_target"]}
   except ValueError:
    return{"Date":row["date"], "Clicks":0}
 


# so here I couldn't use 'clicks_csv' for mapping because the parameter didn't accept a list, so I had to input the specific directory path. 
rows = read_database('data/clicks')
get_rows = map(get_columns, rows)


# now I need to count the number of clicks





