vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 {"name": "aubergine"},
 {"name": "hamburger"},
 {"name": "walrus"},
]

# Write header file to CSV
import csv

with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'length'])

# Loop through each vegetable
# for each vegetable, write a row to the CSV
	for wtf in vegetables:
		#name = wtf['name']
		#length = len(name)
		data_row = [wtf['name'], len(wtf['name'])]
		writer.writerow(data_row)