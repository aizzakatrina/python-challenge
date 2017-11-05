# Aizza Asuncion
# UCBSAN1010Data
# Unit 3 homework - PyBoss
# Dr. Spronck
# 5 October 2017

import os
import csv
import datetime

# create lists to store data
emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

# create dictionary of states
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# get file path and name
path = input("Enter the file path and/or file name: ")
filename = os.path.join(path)

# open file in read mode and store contents in variable filedata
with open(filename, newline = '') as filedata:
    
    # specify delimiter and store contents in variable
    csvreader = csv.reader(filedata, delimiter = ',')

    # skip header
    next(csvreader, None)

    for row in csvreader:  

        # get employee id
        emp_id_data = row[0]

        # add employee id to list
        emp_id.append(emp_id_data)

        # get full name as string and store in variable
        full_name = row[1]

        # split full name into first and last names and store in list
        names = full_name.split()

        # store first and last name to variables
        name_first = names[0]
        name_last = names[1]

        # add to first and last name lists
        first_name.append(name_first)
        last_name.append(name_last)

        # get DOB
        dob_raw = row[2]

        # change DOB format from yyyy-mm-dd to mm/dd/yyyy
        dob_converted = datetime.datetime.strptime(dob_raw, '%Y-%m-%d').strftime('%m/%d/%Y')

        #add formatted date to DOB list
        dob.append(dob_converted)
        
        # get SSN as string and store in variable
        ssn_raw = row[3]

        # split ssn string by hyphen and store in list
        ssn_split = ssn_raw.replace('-', ' ').split(' ')

        # change SSN format
        ssn_formatted = "***-**-" + ssn_split[2]

        # add formatted ssn to ssn list
        ssn.append(ssn_formatted)

        # get state
        state_raw = row[4]

        # find state in dictionary and store value in variable
        if state_raw in us_state_abbrev.keys():
            state_abbreviated = us_state_abbrev[state_raw]
        
        # add abbreviated state to list
        state.append(state_abbreviated)

# zip lists together
roster = zip(emp_id, first_name, last_name, dob, ssn, state)

# specify output file to write results to
output_file = os.path.join('results.csv')

# open file in write mode and store contents to variable
with open(output_file, 'w', newline='') as resultsfile:

    csvwriter = csv.writer(resultsfile)

    # write header in file
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # write zipped rows
    csvwriter.writerows(roster)