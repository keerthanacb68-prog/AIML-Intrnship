import csv 
print("Name of th students who are passed/n")
with open("student.csv","r") as file:
  csv_file = csv.DictReader(file)
  for row in csv_file:
    if row['status']=="pass":
      print(f"{row['Name']}")