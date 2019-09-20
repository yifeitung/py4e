# This is the Assignment for Chapter 11.

# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text
#and numbers. You will extract all the numbers in the file and compute
#the sum of the numbers.

# Data Files
# We provide two files for this assignment. One is a sample file where
# we give you the sum for your testing and the other is the actual data
# you need to process for the assignment.

# Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt (There
#are 90 values with a sum=445833)
# Actual data: http://python-data.dr-chuck.net/regex_sum_187115.txt
# (There are 92 values and the sum ends with 404)

# Handling The Data
# The basic outline of this problem is to read the file, look for integers using
# the re.findall(), looking for a regular expression of '[0-9]+' and then
# converting the extracted strings to integers and summing up the integers.

import re

name=input('Enter file:')
if len(name)<1:
    name="regex_sum_187115.txt"
# Guardian
try:
    handle=open(name)
except:
    print('File cannot be opened:',name)
    exit()

sum=0
numbers=list()
for line in handle:
    line=line.strip()
    x=re.findall("[0-9]+",line)
    if len(x)<1:
        continue
    for number in x:
        numbers.append(number)
        fnumber=int(number)
        sum=sum+fnumber
print(sum)
