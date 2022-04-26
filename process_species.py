import pandas as pd
import math
import numpy as np
import os

countries = []
with open('countries.txt', 'r') as f:
	countries = f.readlines()
	countries = [country[:-1].lower() for country in countries]

data = pd.read_csv("all-mammals.csv", encoding="ISO-8859-1")
data = data[['Order', 'Family','Genus','Species','CommonName','TypeLocality']]
print(data.columns)


keep_indices = []
for index, row in data.iterrows():
	locs = row['TypeLocality']
	if not isinstance(locs,str) : continue
	locs = locs.split()
	containCountry = False
	for loc in locs:
		if loc.lower() in countries:
			containCountry = True
	if not containCountry : continue
	print(row)
	if not isinstance(row['CommonName'],str) : continue
	if not isinstance(row['Order'],str) : continue
	if not isinstance(row['Family'],str) : continue
	if not isinstance(row['Genus'],str) : continue
	if not isinstance(row['Species'],str) : continue
	keep_indices.append(index)

data = data.iloc[keep_indices]

data['Order'] = data['Order'].str.lower()
data['Family'] = data['Family'].str.lower()
data['Genus'] = data['Genus'].str.lower()
data['Species'] = data['Species'].str.lower()

with open('UniqueOrder.txt', 'w') as f:
	orderList = [order+'\n' for order in data['Order'].unique()]
	f.writelines(orderList)

with open('UniqueFamily.txt', 'w') as f:
	familyList = [family+'\n' for family in data['Family'].unique()]
	f.writelines(familyList)

with open('UniqueGenus.txt', 'w') as f:
	genusList = [genus+'\n' for genus in data['Genus'].unique()]
	f.writelines(genusList)

with open('UniqueSpecies.txt', 'w') as f:
	speciesList = [species+'\n' for species in data['Species'].unique()]
	f.writelines(speciesList)


data.to_csv("good-mammals.csv")
print(len(data))

with open('good-mammals.txt', 'w') as f:
	for index, row in data.iterrows():
		order = row['Order']
		family = row['Family']
		genus = row['Genus']
		species = row['Species']
		commonName = row['CommonName']
		habitat = row['TypeLocality']
		f.write(f'{order}#{family}#{genus}#{species}#{commonName}#{habitat}\n')


