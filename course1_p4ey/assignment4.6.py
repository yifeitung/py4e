def computepay(h,r):
    if h>40:
        reg=h*r
        otg=(h-40)*(r*0.5)
        tp=reg+otg
    else:
        tp=reg
    return tp

hrs = input("Enter Hours:")
ratehour=input("Enter Rate:")

try:
    h=float(hrs)
    r=float(ratehour)
except:
    print("Enter a valid float value")
    quit()

p = computepay(h,r)
print(p)
