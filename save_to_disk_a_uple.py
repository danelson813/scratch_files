import csv

data = [
    ("Name", "Age", "City"),
    ("Alice", 30, "New York"),
    ("Bob", 24, "London"),
    ("Charlie", 35, "Paris")
]

with open('list_of_tuples.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data)  # if only one, use writerow