# Assignment 9.4
# Write a program to read through the mbox-short.txt and figure out who has sent
# the greatest number of mail messages. The program looks for 'From ' lines and
# takes the second word of those lines as the person who sent the mail. The
# program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to
# find the most prolific committer.

name=input('Enter a file name:')
handle=open(name)
emaildictionary=dict()         # create an empty dictionary
for line in handle:
    line=line.strip()
    if line.startswith('From') and not line.startswith('From:'): # find the line we want
        targetline=line.split() # split the line
        emails=targetline[1:2]  # find the email address
        for email in emails:
            emaildictionary[email]=emaildictionary.get(email,0)+1

# print(emaildictionary)   # print out the dictionary

bigemail=None
bigcount=None
for email,count in emaildictionary.items():
    if bigemail is None or count>bigcount:
        bigemail=email
        bigcount=count

print(bigemail, bigcount)

'''
for line 18-19, you can read book 'Python for everybody' Page.107. use get ()
method is same to use if/else loop. The idea is to traverses the string. Each time through
the loop, if the character email is not in the dictionary, we create a new itmen with key 'email'
and the initial value 1 (since we have seen this email once). If email is already in the
dictionary, we increment emaildictionary[email].

get() method takes a key and a default value. If the key appears in the dictionary,
get returns the corresponding value; otherwise it returns the default value.
The default value in this case is 0.

'''
## End of the assignment
