#Python Assignment

import define_exoplanet_class
import csv
from itertools import islice


def find_max_and_min_values(dataset, attribute):
    max_value=0
    min_value=0
    value=0
    for row in dataset:
        try:
            value = float(row[attribute])
        except:
            continue
        if value > max_value: max_value = value
        if value < min_value: min_value = value
    return(max_value, min_value)
    
data = []

dExoplanets={}
headers=[]
listg=[]

'''
Reads in the CSV file ignoring comments

def read_data(csv):
    with open(csv, 'r') as csvfile:
        planets_csv = csv.reader(csvfile)
        for line in planets_csv:
    
            if not line[0].startswith('#'): #Remove comments from file
    
                if not line[0].isdigit(): 
                    headers=line
                else:
                    data.append(line)
    return headers,data
'''

#Uncomment as necessary
csv_file_name = 'planets_practice.csv'
#csv_file_name = 'planets.csv'

with open(csv_file_name, 'r') as csvfile:
    n=0
    for line in csvfile.readlines():
        if not line.startswith('#'):
            break
        n+=1
    
with open(csv_file_name, 'r') as csvfile:
    reader = csv.DictReader(islice(csvfile, n, None))
    #print("headers are : " + str(reader.fieldnames))
    #for row in reader:
    #    print(row)
    #    for header, value in row.items():
    #        try:data[header].append(value)
    #        except KeyError:
    #            data[header] = [value]
    data=list(reader)
    
print(data)
    
#closest_star, furthest_star = find_max_and_min_values(data,"st_dist")
#for row in data:
#    for key, value in row:
#        if value == closest_star:
#            print(key)