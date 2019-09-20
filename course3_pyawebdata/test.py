# This file is used to test a program. You can ignore this file.
import re
x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y=re.findall('\S+?@\S+',x)
print(y)
