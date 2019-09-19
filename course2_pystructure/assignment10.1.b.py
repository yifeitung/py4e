# Assignment 10.1 Method B
'''
Revise a previous program as follows: Read and parse the "From" lines and
pull out the addresses from the line. Count the number of messages from
each person using a dictionary.

After all the data has been read print the person with the most commits by
creating a list of (count, email) tuples from the dictionary and then sorting
the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
'''

name=input('Enter a file name:')
if len(name)<1:
    name='mbox-short.txt'
# Guardian
try:
    handle=open(name)
except:
    print('File cannot be opened:',name)
    exit()

counts=dict()
for line in handle:
    line=line.strip()
    if line.startswith('From')and not line.startswith('From:'):
        targetline=line.split()
        targetemail=targetline[1]
        # print(targetemail)
        counts[targetemail]=counts.get(targetemail,0)+1
# print(counts)

lst=list()
for k,v in counts.items():
    newsetup=(v,k)
    lst.append(newsetup)
# print(lst)
lst=sorted(lst,reverse=True)
# print(lst)
winner=lst[0]
# print(winner)
print(winner[1],winner[0])
