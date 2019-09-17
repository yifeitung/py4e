'''
# Exercise 8.6
# Rewrite the program that prompts the user for a list of numbers
# and prints out the maximum and minimum of the numbers at the end when the user
# enters "done". Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum
# numbers after the loop completes.

Enter a number: 6
Enter a number: 2
Enter a number: 9
Enter a number: 3
Enter a number: 5
Enter a number: done
Maximum: 9.0
Minimum: 2.0

'''
numlist=list()
while True:                          # infinite loop
    inp=input('Enter a number:')
    if inp=='done':    # when input is 'done',skip all and go diectly to caculate maximum and minimum
        break
    value=float(inp)                 # change the string in to a floating point
#   print(value)
    numlist.append(value)        # store the number the user enters into a list
max=max(numlist)                # find the maximum number in the list
min=min(numlist)               # find the minimum number in the list
print('Maximum:', max)
print('Minimun:', min)
