srs=input("Enter score:")
try:
    x=float(srs)
except:
    print("Bad score")
    quit()

print(x)
if 0.0<=x<0.6:
    print("F")
elif 0.6<=x<0.7:
    print("D")
elif 0.7<=x<0.8:
    print("C")
elif 0.8<=x<0.9:
    print("B")
elif 0.9<=x<1.0:
    print("A")
else:
    print("Bad score")
