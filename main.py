import csv

with open("d:\Company_Data.csv", mode = "r") as file:

    csv_file =  csv.reader(file)
    for lines in csv_file:
        print(lines)