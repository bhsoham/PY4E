fname=input('Enter file name:')
fhand=open(fname)
sub='X-DSPAM-Confidence'
count=0
total=0
for line in fhand:
    line=line.strip()
    if sub in line:
        index=line.find(':')
        data=line[index+1:]
        fdata=float(data)
        total=total+fdata
        count=count+1
avg=total/count
print('Average spam confidence:',avg)