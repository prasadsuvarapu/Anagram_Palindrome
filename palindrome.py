import csv
# Reading data from csv file provided.
with open('dataFile.csv') as check_file:
    palindrome = csv.reader(check_file, delimiter=',', quotechar='|')
    row = []
    for key in palindrome:
        row.extend(key)
# Printing the input data given.
    print('this is row:', row)
# Function definition to get palindromes.
from collections import defaultdict
def get_palindrome(row):
    temp = defaultdict(list)    # Created a defaultdict to store reversed list of input.
    result = defaultdict(list)  # Created another defaultdict to store the reversed of reversed string.
    for rev_get in row:
        result[''.join(reversed(rev_get.lower()))].append(rev_get)
    for chk_strng in result:
        temp[''.join(reversed(chk_strng.lower()))].append(chk_strng)
    # Created lists to stores keys of the above dicts.
    compStrng = list(result.keys())
    print('compstring:',compStrng)
    compStrng2 =list(temp.keys())
    print('compstring2:',compStrng2)
    res =[]
    # Final output loop block.
    for i in range(len(compStrng)): #index comparision
        if compStrng[i] == compStrng2 [i]:
            res.append(compStrng2[i])
            print('palindrome:',res)
    print(res)

    return res
print('End of File and Palindromes are:', get_palindrome(row))
