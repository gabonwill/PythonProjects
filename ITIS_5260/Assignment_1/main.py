import pandas as pd
import datetime
from geopy.distance import geodesic
import csv
import os

# Files that need to be read
files = ['dataset/datalog.csv', 'dataset/dept_resources.csv', 'dataset/employee_details.csv', 'dataset/office_locations.csv']

def fixdate(d, sample):
    if sample == 'data':
        d = pd.DataFrame(d['Datetime'].str.split(' ',1).tolist(),columns=['Date','Time'])
    else:
        d = pd.DataFrame(d['End Date'].str.split(' ',1).tolist(),columns=['EndDate'])
    return d


data = pd.read_csv(files[0])
data = data.join(fixdate(data,'data'))
employee = pd.read_csv(files[2])
employee = employee.join(fixdate(employee, 'employee'))

department = pd.read_csv(files[1])
office_location = pd.read_csv(files[3])

# Unauthorized access
access = pd.merge(data,employee,on=['EmployeeID'])
access = access[access['Action'] == 'login']
access['Date'] = pd.to_datetime(access['Date'])
access['EndDate'] = pd.to_datetime(access['EndDate'])
# print(access)
access = access.loc[(access['Date'] > access['EndDate'])]
print(access['EmployeeID'], "Number found " +  str(len(access)))

# Employee logins in from a different location
location = pd.merge(employee, data, on=["EmployeeID"])
location = location.loc[((geodesic((location['Home Latitude'], location['Home Longitude']), (location['Latitude'], location['Longitude'])).miles > 1))]
print(location['EmployeeID'], "Number found " + str(len(location) ))

# Access outside of department
department = department.join(pd.DataFrame(department['Department'].str.split(' ',1).tolist(),columns=['DepartmentResources']))
department = department.join(pd.DataFrame(department['ResourceID'].str.split(' ',1).tolist(),columns=['Resources']))
departmt = pd.merge(data, employee, department)
# departmt = departmt.loc[(departmt['Department'] != departmt['DepartmentResources'])]
# departmt = departmt.loc[(departmt['ResourceID'] == departmt['Resource'])]
# print(departmt['EmployeeID'], "Number of: " + str(len(departmt)))
