import csv
# Reading data from csv file provided.
with open('dataFile.csv') as check_file:
    palindrome = csv.reader(check_file, delimiter=',', quotechar='|')
    row = []
    for key in palindrome:
        row.extend(key)
# Printing the input data given.
print('Input data from the file is:',row)
# Function definition to get anagrams.
from collections import defaultdict
def anagram_check_string(row):
    test = defaultdict(list)    # Created a defaultdict to store reversed list of input.
    for check_string in row:

        test[''.join(sorted(check_string.lower()))].append(check_string)
    # Output anagram is returned to the function.
    return [a for b, a in test.items() if len(a) > 1]
print('Anagrams in the file are:', anagram_check_string(row))
