def computepay(hrs,rate):
    rpay= hrs*rate
    if(hrs>40):
        xpay= 0.5*(hrs-40)*rate
        pay= rpay + xpay
    else:
        pay=rpay
    return pay
    
h= float(input('Enter Hours:'))
r= float(input('Enter Rate:'))
p= computepay(h, r)
print('Pay:',p)

