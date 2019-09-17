'''
# Open the file mbox-short.txt and read it line by line. When you
# find a line that starts with 'From ' like the following line:

#       From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# You will parse the From line using split() and print out the second
# word in the line (i.e. the entire address of the person who sent the
# message). Then you will also count the number of From (not From:) lines and
# print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
'''
fname=input('Enter a file name:')
fh=open(fname)
lst=list()
count=0
for line in fh:
    line=line.strip()
    if line.startswith('From') and not line.startswith('From:'):
        words=line.split()
        email=words[1:2]
        count=count+1
        for element in email:
            lst.append(element)     # add all elements into a list
for p in lst:                       # travese the elements of a list using for loop
    print(p)
# print(count)
print('There were', count, 'lines in the file with From as the first word')
