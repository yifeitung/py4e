# You can find '0' first and then find '5'
text = "X-DSPAM-Confidence:    0.8475";
ats=text.find('0')
print(ats) #print is optional, do not report print when you upload your results
atf=text.find('5')
print(atf) #print is optional, do not report print when you upload your results
stirpr=text[ats-1:atf+1]
print(stirpr) #print is optional
flotpr=float(stirpr)
print(flotpr)

# You can also use the method introduced in the video, which is to search ':'
text = "X-DSPAM-Confidence:    0.8475";
stir1=text.find(':')
num=text[stir1+1:] # If you omit the second index, the slice goes to the end of the string
floatnum=float(num)
print(floatnum)
