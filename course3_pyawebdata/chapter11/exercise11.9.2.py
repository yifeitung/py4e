# This is the Exercise 11.9.2 for Book 'Python for Everybody: Exploring Data
# in Python 3'

# Write a program to look for lines of the form
# "New Revision: 39772"
# and extract the number from each of the lines using a regular expression and
# the findall() method. Compute the average of the numbers and print out the average.

# Enter file: mbox.txt
# 38549.7949721

# Enter file: mbox-short.txt
# 39756.9259259

import re
name=input("Enter file:")
if len(name)<1:
    name="mbox.txt"
# Guardian
try:
    handle=open(name)
except:
    print("File cannot be opened:",name)
    exit()

count=0
sum=0
for line in handle:
    line=line.strip()
    x=re.findall('^New Revision: ([0-9]+)',line)
    if len(x)<1:   # Remember that if there is a blank line, just continue the loop until we find a number
        continue
    for number in x:
        count=count+1
        intnumber=int(number)
        sum=sum+intnumber

print("Average:",sum/count)
