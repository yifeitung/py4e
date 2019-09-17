## This is quiz and answer keys for Chapter 9

'''
1. How are Python dictionaries different from Python lists?
ANSWER: Python lists maintain order and dictionaries do not maintain order.

2. What is a term commonly used to describe the Python dictionary feature in other
programming languages?
ANSWER: Associative arrays.

3. What would the following Python code print out?

stuff=dict()
print(stuff['candy'])

ANSWER: The program would fail with a traceback.

4. What would the following Python code print out?

stuff=dict()
print(stuff.get('candy',-1))

ANSWER: -1

5. (T/F) When you add items to a dictionary they remain in the order in which you
added them.
ANSWER: False.

6. What is a coomon use of Python dictionaries in a program?
ANSWER: Buidling a histogram counting the occurrences of various strings in a file.

7. Which of the following lines of Python is equivalent to the following
sequence of statements assuming that counts is a dictionary?

if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1

ANSWER: counts[key]=counts.get(key,0)+1

8. In the following Python, what does the for loop iterate through?

x = dict()
...
for y in x :
     ...

ANSWER: It loops through the keys in the dictionary.

9. Which method in a dictionary object gives you a list of the values in the dictionary?
ANSWER: values()

10. What is the purpose of the second parameter of the get() method for Python dictionaries?
ANSWER: To provide a default value if the key is not found.

'''
## End of the quiz for Chapter 9. 
