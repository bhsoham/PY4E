fname=input('Enter file name:')
fhand=open(fname)
romeo=list()
for line in fhand:
    line=line.rstrip()
    pieces=line.split()
    for word in pieces:
        if word not in romeo:
            romeo.append(word)
romeo.sort()
print(romeo)