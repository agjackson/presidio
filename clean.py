import csv

read = '/Users/arlenagjackson/Documents/GitHub/presidio/Aran_output.txt'
write = '/Users/arlenagjackson/Documents/GitHub/presidio/Aran.csv'
  
#with open(read, 'r') as reader, open(write, 'w') as writer:
with open(write, mode='w',newline='') as f:
    # Read and print the entire file line by line
    fieldnames = ['Speaker', 'Speech']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

"""
field_names = ['Row', 'Speaker', 'Speech']
  
cars = [
{'No': 1, 'Company': 'Ferrari', 'Car Model': '488 GTB'},
{'No': 2, 'Company': 'Porsche', 'Car Model': '918 Spyder'},
{'No': 3, 'Company': 'Bugatti', 'Car Model': 'La Voiture Noire'},
{'No': 4, 'Company': 'Rolls Royce', 'Car Model': 'Phantom'},
{'No': 5, 'Company': 'BMW', 'Car Model': 'BMW X7'},
]
  
with open('Aran.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(cars)"""