import csv
# Reading data from csv file provided.
with open('anagram.csv') as check_file:
    palindrome = csv.reader(check_file, delimiter=',', quotechar='|')
    row = []
    for key in palindrome:
        row.extend(key)
# Printing the input data given.
print('Input data from the file is:',row)

# Function definition to get anagrams.
from collections import defaultdict
temp = defaultdict(list)    # Created a defaultdict to store reversed list of input.
result = defaultdict(list)  # Created another defaultdict to store the reversed of reversed string.
def anagram_check_string(row):
    test = defaultdict(list)    # Created a defaultdict to store reversed list of input.

    for check_string in row:

        result[''.join(sorted(check_string.lower()))].append(check_string)
    # Output anagram is returned to the function.
    return [a for b, a in result.items() if len(a) > 1]

# Function definition to get palindromes.
def get_palindrome(row):

    for rev_get in row:
        result[''.join(reversed(rev_get.lower()))].append(rev_get)
    for chk_strng in result:
        temp[''.join(reversed(chk_strng.lower()))].append(chk_strng)
    # Created lists to stores keys of the above dicts.
    compStrng = list(result.keys())
    compStrng2 =list(temp.keys())
    res =[]
    # Final output loop block.
    for i in range(len(compStrng)): #index comparision
        if compStrng[i] == compStrng2 [i]:
            res.append(compStrng2[i])
    return res
print('Anagrams in the file are:', anagram_check_string(row))
print('End of File and Palindromes are:', get_palindrome(row))