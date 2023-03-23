
# I import the os so I can loop through it
import os
# I need to read the data in the CSV files first, so I import CSV for that matter. It's important that the database files are placed in the same folder as the code. 
import csv

def read_database(data):
    # I pass it an empty list that will receive all of the data found in the loop
    csv_files = []
    # for each file you find in the 'data' folder, list it.
    for file in os.listdir(data):
        # if the file is in csv format, open it and store the data with the name csvfile
        if file.endswith('.csv'):
            with open(os.path.join(data, file), newline='') as csvfile:
                # store the csvfile data in the csv reader object. dictreader embedded function return an orderes dictionary for each row.
                reader = csv.DictReader(csvfile)
                # using the extend method to add the rows from each CSV file to the csv_file. If I used append instead of extend,  because I want to add all the dictionaries to the list individually and not the entire reader object as one element.
                csv_files.extend(reader)
    # I get the list with the data already ordered by row. 
    return csv_files

folder1_csv = read_database('data/clicks')
folder2_csv = read_database('data/users')
all_csv_files = folder1_csv + folder2_csv

print(folder2_csv)



