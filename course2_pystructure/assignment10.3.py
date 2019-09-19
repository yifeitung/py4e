# Assignment 10.3

'''
Write a program that reads a file and prints the letters in decreasing order
of frequency. Your program should convert all the input to lower case and
only count the letters a-z. Your program should not count spaces, digits,
punctuation or anything other than the letters a-z. Find text samples from
several different languages and see how letter frequency varies between
languages. Compare your results with the tables at

wikipedia.org/wiki/Letter_frequencies.

'''
# You need first import string module in this assignment"
import string
name=input('Enter a file name:')
# use space to test a file named '3wishes.txt'
if len(name)<1:
    name='3wishes.txt'
# Guardian
try:
    handle=open(name)
except:
    print('Error! Invalid file name.')
    exit()

count=0
wlst=list()
lettersdict=dict()
for line in handle:
    line=line.strip()
    line=line.lower()
    # Remove punctuation and numbers in each line and set upper case into lower case
    line=line.translate(str.maketrans('','',string.punctuation))
    line=line.translate(str.maketrans('','',string.digits))
    words=line.split()
    # print(words)
    for word in words:
        wlst.append(word)
        for letter in word:
            count=count+1 # count each letter
            lettersdict[letter]=lettersdict.get(letter,0)+1
# print(lettersdict)
# print(count)

letterlist=list()
for k,v in lettersdict.items():
    newsetup=(v/count,k) # we compute the relative frequency for each letter
    letterlist.append(newsetup)
# print(letterlist)
letterlist=sorted(letterlist,reverse=True)

top_five_winner=letterlist[0:5]
for p in top_five_winner:
    print(p[1],p[0])

# Analysis
'''
From Wikipedia, we know that the top five letter in the English language are
e (12.702%),t(9.056%),a(8.167%),o(7.507%),i(6.966%)

By using the sample file '3wishes.txt', the top five letter are: e,t,h,o,a
By using the sample file '3gables.txt', the top five letter are: e,t,o,a,i

The article in '3gables.txt' is longer than the article in '3wishes.txt'.
'''
