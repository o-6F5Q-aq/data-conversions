#Read veggies.csv
import csv

with open('veggies.csv') as f:
	#Convert to JSON
	reader = csv.DictReader(f)
	vegetables = list(reader)

#Write to JSON
import json

with open('veggies.json', 'w') as f:
	json.dump(vegetables, f, indent=2)