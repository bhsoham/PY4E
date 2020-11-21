hrs= float(input('Enter Hours:'))
rate= float(input('Enter Rate:'))
rpay= hrs*rate
if(hrs>40):
    xpay= 0.5*(hrs-40)*rate
    pay= rpay + xpay
else:
    pay=rpay
print('Pay:',pay)