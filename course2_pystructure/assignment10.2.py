# Assignment 10.2
# Write a program to read through the mbox-short.txt and figure out
# the distribution by hour of the day for each of the messages. You can
# pull the hour out from the 'From ' line by finding the time and then
# splitting the string a second time using a colon.
#            From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the
# counts, sorted by hour as shown below.

name=input('Enter a file name:')
if len(name)<1:
    name=('mbox-short.txt')
# Guardian
try:
    handle=open(name)
except:
    print("File cannot be opened:", name)
    exit()

counts=dict()
for line in handle:
    line=line.strip()
    if line.startswith('From')and not line.startswith('From:'):
        targetline=line.split()
        targettime=targetline[5]
        colon=targettime.find(':')
        targethour=targettime[:colon]
        # print(targethour)
        counts[targethour]=counts.get(targethour,0)+1
# print(counts)
lst=list()
for k,v in counts.items():
    newsetup=(k,v)
    lst.append(newsetup)
# print(lst)
lst=sorted(lst)
# print(lst)
for key,value in lst:
    print(key,value)
