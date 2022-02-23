import csv
from dataclasses import dataclass
dataset_1 = []
dataset_2 = []

with open("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars.csv","r")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open("https://en.wikipedia.org/wiki/List_of_brown_dwarfs.csv","r")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)
    
headers1 = dataset_1[0]
planetData1 = dataset_1[1:]
headers2 = dataset_2[0]
planetData2 = dataset_2[1:]

headers = headers1 + headers2
planetData = []
for index, datarow in enumerate(planetData1):
    planetData.append(planetData1[index]+ planetData2[index])

with open("final.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetData)

