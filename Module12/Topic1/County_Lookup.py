import csv
from Module12.Topic1.County_List import CountyList

with open('CensusData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # initialize empty dictionary
    county={}
    for row in csv_reader:
        # skip the first line in the file because it is the header
        if line_count == 0:
            line_count += 1
            continue
        if str(row[0]) == '':
            line_count += 1
            continue
        # create an item in dictionary county with a key of the county name and a value of the object
        county[str(row[1])] = CountyList(row[2], row[3], row[4], row[5], row[6])


print(county["Dallas"].population_data("Dallas"))

pop_sum = 0
for key in county:
    pop_sum += int(county[key].population.replace(',',''))
print(f"Total Population: {pop_sum:,}")
