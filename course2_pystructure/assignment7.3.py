'''
Sometimes when programmers get bored or want to have a bit of fun, they add
a harmless Easter Egg to their program
(en.wikipedia.org/wiki/Easter_egg_(media)). Modify the program that prompts
the user for the file name so that it prints a funny message when the user
types in the exact file name 'na na boo boo'. The program should behave
normally for all other files which exist and don't exist. Here is a sample
execution of the program:
python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
We are not encouraging you to put Easter Eggs in your programs - this is just
an exercise.
'''

# First input the file name
fname=input('Enter the file name:')
count=0

if fname=="na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit() # Exit the program when have input 'na na boo boo'

try:
    fh=open(fname)
except:
    print('File cannot be opened:',fname)
    exit() # Exit the program when the file cannot be opened

for line in fh:
    if line.startswith('Subject:'):
        count=count+1
print('There were',count, 'subject lines in', fname)
