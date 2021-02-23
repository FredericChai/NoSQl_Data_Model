# Goes through a CSV an build a JSON out of it. 

import csv
import json

# create a json file (with write access)
jsonfile = open('file.json', 'w')

# hold components
comp = []

# open and load the csv
with open('updated2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # iterates through all the rows from the csv
    for row in readCSV:
            # row[0] = component
            # row[1] = version
            # row[2] = package manager
            print(row)
            temp = {'component':{row[2]:{'name':row[0], 'version':row[1]}}}  
            print(temp)   
            comp.append(temp)
            json_string = json.dumps(temp)
            print(json_string)   
print("##########")
json.dump(comp, jsonfile, sort_keys=True, indent=4, separators=(',', ': '))
print(jsonfile)


# "component": {
#     "nuget.org": {
#         "name": "EntityFramework",
#         "version": "6.1.3"
#     }
# }    


 
