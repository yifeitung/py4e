'''
# Open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split() method. The
# program should build a list of words. For each word on each line check
# to see if the word is already in the list and if not append it to the
# list. When the program completes, sort and print the resulting words
# in alphabetical order.

You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
'''
fname = input("Enter file name: ")
fh = open(fname)
lst=list()                         # list for the desired output
for line in fh:                    # to read every line of file
#    print(line.strip())           # print is optional, use print to check if line is read
    words=line.split()             # turn the line into a list of words
#    print(words)                  # print is optional, use print to check if words are cutted
    for element in words:          # check every element in words
        if element in lst:         # if element is in the list
            continue
        else:                      # if element is not in the list
            lst.append(element)    # append that element
lst.sort()                         # sort the list in alphabetical order
print(lst)                         # print the list

'''
This is a very tricky question and takes time to think about it very carefully.
Basically, what I do in this assignment is to think about how to cut lines first
and then cut the words for each line. After that, we need to create a loop to check
if the element is alrealy in the list. If the element is already in the list, we
do nothing, otherwise, we add that element into the list.
'''
