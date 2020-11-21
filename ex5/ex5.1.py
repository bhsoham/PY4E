num=0
sum=0.0
while True:
    sval=input('Enter a number: ')
    if(sval=='done'):
        break
    try:
        fval=float(sval)
    except:
        print('Invalid input')
        continue
    #print(fval)
    num=num+1
    sum=sum+fval
#print('all done')
print(sum,num,sum/num)