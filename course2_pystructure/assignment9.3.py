# Assignment 9.3

'''
Write a program to read through a mail log, build a histogram
using a dictionary to count how many messages have come from each email
address, and print the dictionary.

Enter file name: mbox-short.txt
{'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3,
'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5,
'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1,
'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1,
'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}

'''
name=input('Enter a file name:')
try:
    handle=open(name)
except:
    print('File cannot be opened:', name)
    exit()

emaildictionary=dict()
for line in handle:
    line=line.strip()
    if line.startswith('From') and not line.startswith('From:'):
        targetline=line.split()
        emails=targetline[1:2]
        for email in emails:
            emaildictionary[email]=emaildictionary.get(email,0)+1
print(emaildictionary)
