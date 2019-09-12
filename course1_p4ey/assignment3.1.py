hrs=input("Enter Hours:")
h=float(hrs)
hrate=input("Enter Rate:")
rate=float(hrate)
if h>40:
    reg=h*rate
    otp=(h-40)*(rate*0.5)
    tp=reg+otp
else:
    tp=h*rate
print("Pay:",tp)
