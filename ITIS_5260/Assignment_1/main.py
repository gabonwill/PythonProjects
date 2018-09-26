import pandas as pd
import csv
import os

# Files that need to be read
files = ['dataset/datalog.csv', 'dataset/dept_resources.csv', 'employee_details.csv', 'office_locations.csv']

## First file as an example
## Reference for reading CVS's
## https://docs.python.org/3/library/csv.html

# This reading from the datalog.csv
with open(files[0], newline='') as file:
    data = csv.reader(file, delimiter=',')
    for item in data:
        print(item)
        # From here you will want to store the item somewhere

# You fix this one
# This reading from the employee_details.csv
with open(files[2], newline='') as file:
    data = csv.reader(file, delimiter=',')
    # for item in data:

