# This is quiz and answer keys for Chapter 10

'''
1. What is the difference between a Python tuple and Python list?
ANSWER: Lists are mutable and tuples are not mutable.

2. Which of the following methods work both in Python lists and Python tuples?
ANSWER: index()
# Tuples cannot be sorted because tuples are not mutable.

3. What will end up in the variable y after this code is executed?

x,y=3,4

ANSWER: 4

4. In the following Python code, what will end up in the variable y?

x={'chuck':1,'fred':42,'jan':100}
y=x.items()

ANSWER: A list of tuples.

5. Which of the following tuples is greater than x in the following Python sequence?

x = (5, 1, 3)
if ??? > x :
   ...

ANSWER: (6,0,0)

6. What does the following Python code accomplish, assuming the c is a non-empty dictionary?

tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )

ANSWER: It creates a list of tuples where each tuple is a value, key pair.

7. If the variable data is a Python list, how do we sort it in reverse order?
ANSWER: data.sort(reverse=True)

8. Using the following tuple, how would you print 'Wed'?

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

ANSWER: print(days[2])

9. In the following Python loop, why are there two iteration variables (k and v)?

c = {'a':10, 'b':1, 'c':22}
for k, v in c.items() :
    ...

ANSWER: Because the items() method in dictionaries returns a list of tuples.

10. Given that Python lists and Python tuples are quite similar - when might you
prefer to use a tuple over a list?
ANSWER: For a tempirary variable that you will use and discard without modifying.

'''
# End of the quiz.
