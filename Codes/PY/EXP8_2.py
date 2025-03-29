import re
phone_book='''Rao Jayesh 9876543210
Patel Kiran 9123456789
Rao Kunal 8765432109
Sharma Rohan 9812345678
Rao Kiran 9988776655'''
with open("phonebook.txt", "w") as file:
    file.write(phone_book)
with open("phonebook.txt", "r") as file:
    data=file.readlines()
rao=r"\bRao\s+(J|K)\w*\s+\d+"
matches=[line.strip() for line in data if re.search(rao, line)]
print("Entries with Surname 'Rao' and First Name Starting with 'J' or 'K': ")
for match in matches:
    print(match)
