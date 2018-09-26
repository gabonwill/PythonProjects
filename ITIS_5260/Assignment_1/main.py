import pandas as pd
import csv
import os

# Files that need to be read
files = ['dataset/datalog.csv', 'dataset/dept_resources.csv', 'dataset/employee_details.csv', 'dataset/office_locations.csv']

# Read this tutorial
## https://www.datacamp.com/community/tutorials/pandas-read-csv
data = pd.read_csv(files[0])
employee = pd.read_csv(files[2])
department = pd.read_csv(files[1])
office_location = pd.read_csv(files[3])

print(data)
