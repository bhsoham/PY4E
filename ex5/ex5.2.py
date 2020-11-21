max= None
min= None
while(True):
    sval=input('Enter a number: ')
    if(sval=='done'):
        break
    try:
        ival=int(sval)
    except:
        print('Invalid input')
        continue
    if(max is None or min is None):
        max=ival
        min=ival
    if(ival>max):
        max=ival
    if(ival<min):
        min=ival
print('Maximum is',max)
print('Minimum is',min)