hrs= input('Enter Hours:')
rate= input('Enter Rate:')
try:
    rpay= float(hrs)*float(rate)
except:
    print('Error, please enter numeric input')    
    quit()
        
if(hrs>40):
    xpay= 0.5*(hrs-40)*rate
    pay= rpay + xpay
else:
    pay=rpay
print('Pay:',pay)
