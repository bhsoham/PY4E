fname=input('Enter file name:')
fhand=open(fname)
count=0
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        pieces=line.split() 
        email=pieces[1]
        print(email)
        count=count+1
print('There were',count,'lines in the file with From as the first word')