str= 'X-DSPAM-Confidence: 0.8475'
ipos= str.find(':')
val= str[ipos+1:]
fval= float(val.strip())
print(fval)
