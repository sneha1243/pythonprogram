import csv
with open('departments.csv',newline='')as csvfile:
	data=csv.DictReader(csvfile)
	print("ID Department Name")
	print("_________________")
	for row in data:
		print(row['department_id'],row['department_name'])

