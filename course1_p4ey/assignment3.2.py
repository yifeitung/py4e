hrs=input("Enter Hours:")
hrate=input("Enter Rate:")
try:
    h=float(hrs)
    rate=float(hrate)
except:
    print("Error, please enter a numeric input")
    quit()

print(h,rate)
if h>40:
    reg=h*rate
    otp=(h-40)*(rate*0.5)
    tp=reg+otp
else:
    tp=h*rate
print("Pay:",tp)
