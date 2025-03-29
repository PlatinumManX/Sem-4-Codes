import re
cities="Mumbai Delhi Chennai Jaipur Pune Kolkata Hyderabad Madurai Surat Gandhinagar"
ending_ai=re.findall(r"\b\w*ai\b", cities)
print("Cities Ending with 'ai': ", ending_ai)
starting=re.findall(r"\b(?:Mu|Ma)\w*\b", cities)
print("Cities Starting with 'Mu' or 'Ma': ", starting)
ua=re.findall(r"\b\w{1}u\w*a\w{0,1}\b", cities)
print("Cities with 'u' as second letter and 'a' as second last letter: ", ua)
