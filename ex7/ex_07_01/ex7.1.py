fname=input('Enter the file name:')
fhandle=open(fname)
for line in fhandle:
    line=line.rstrip()
    line=line.upper()
    print(line)
