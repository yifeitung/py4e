# Assignment 9.2
'''
Write a program that categorizes each mail message by which day of the week
the commit was done. To do this look for lines which start with "From", then
look for the third word and then keep a running count of each of the days of
the week. At the end of the program print out the contents of your dictionary
(order does not matter).

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}

'''
name=input('Enter a file name:')
handle=open(name)
datedictionary=dict()              # create a dictionary
for line in handle:
    line=line.strip()
    if line.startswith('From') and not line.startswith('From:'):
        targetline=line.split()
        dates=targetline[2:3]
        for date in dates:
            datedictionary[date]=datedictionary.get(date,0)+1
print(datedictionary)
