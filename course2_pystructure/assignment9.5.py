# Assignment 9.5

'''
This program records the domain name (instead of the address)
where the message was sent from instead of who the mail came from (i.e., the
whole email address). At the end of the program, print out the contents of
your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
['media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7, 'gmail.com': 1,
'caret.cam.ac.uk': 1, 'iupui.edu': 8}

'''
name=input('Enter a file name:')
try:
    handle=open(name)
except:
    print('File cannot be opened:',name)
    exit()

domaindictionary=dict()
for line in handle:
    line=line.strip()
    if line.startswith('From') and not line.startswith('From:'):
        targetline=line.split()
        emails=targetline[1:2]
        for email in emails:
            xh=email.find('@')
            # print(xh)
            domain=email[xh+1:]
            # print(domain)

            if domain not in domaindictionary:
                domaindictionary[domain]=1
            else:
                domaindictionary[domain]=domaindictionary[domain]+1

# Method use get()            
'''
            domaindictionary[domain]=domaindictionary.get(domain,0)+1
'''

print(domaindictionary)
