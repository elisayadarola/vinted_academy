# I import the os so I can loop through it
import os
# I need to read the data in the CSV files first, so I import CSV for that matter. It's important that the database files are placed in the same folder as the code. 
import csv
#I import the reduce function by VS Code suggestions after trying to use reduce without defining it
from functools import reduce

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
                # using the extend method to add the rows from each CSV file to the csv_file.  I used extend instead of append, because I want to add all the dictionaries to the list individually and not the entire reader object as one element.
                csv_files.extend(reader)        
               
    # I get the list with the data already ordered by row. 
    return csv_files

#attributing the data to a variable to be called or used later if necessary. 
clicks_csv = read_database('data/clicks')
users_csv = read_database('data/users')
all_user_data = clicks_csv + users_csv
# print(f"the count is: {clicks_csv.count(read_database('data/clicks'))}")
# print(all_user_data)

# here starts the mapping of the info. I will need two parameters for the map function, so the first will be the function obtaining two rows containing the date and the clicks info
# def get_columns(row):
#    try:
#     return{"Date":row["date"], "Clicks":row["click_target"]}
#    except ValueError:
#     return{"Date":row["date"], "Clicks":0}

def get_columns(row):
   
    if row["click_target"] != "":
        return 1
    else:
        return 0
   

click_count = map(get_columns, clicks_csv)
total_count = reduce(lambda a,b : a + b, click_count)

print(total_count)

# def clicks_per_date(rows):
#     click_count = {}
#     for row in rows:
#         date = row["Date"]
#         clicks = int(row["Clicks"])
#         if date in click_count:
#             click_count[date] += clicks
#         else:
#             click_count[date] = clicks
#     return [{"Date": date, "count": count} for date, count in click_count.items()]

# print(clicks_per_date)

# And then i map the rows. So here I couldn't use 'clicks_csv' for mapping because the parameter didn't accept a dictionary, so I had to input the specific directory path. 

get_rows = map(get_columns, clicks_csv)
#so for a dictionary we use len() to instead of count
# for row in get_rows:
#             clicks_value = row["Clicks"]
#             print(row, len(clicks_value))
          


# now I need to count the number of clicks
# import csv
# import os

# # Function to read data from CSV files into a list of dictionaries
# def read_database(data):
#     csv_files = []
#     for file in os.listdir(data):
#         if file.endswith('.csv'):
#             with open(os.path.join(data, file), newline='') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 csv_files.extend(reader)        
#     return list(csv_files)

# # Read clicks data into a list of dictionaries
# clicks = read_database('data/clicks')

# # Extract "date" and "click_target" columns and count clicks for each date
# click_counts = {}
# for row in clicks:
#     date = row["date"]
#     clicks = int(row["click_target"])
#     if date in click_counts:
#         click_counts[date] += clicks
#     else:
#         click_counts[date] = clicks

# # Write results to CSV file
# with open('data/total_clicks.csv', 'w', newline='') as csvfile:
#     fieldnames = ['date', 'count']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for date, count in click_counts.items():
#         writer.writerow({'date': date, 'count': count})
