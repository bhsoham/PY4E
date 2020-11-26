fname=input("Input the name of the file: ")
fhandle=open(fname)

people=list()

for line in fhandle:
    if line.startswith("From: "):
        words=line.split()
        people.append(words[1])


counts=dict()

for person in people:
    counts[person]=counts.get(person,0)+1


maxCount=None
maxPerson=None

for k,d in counts.items():
    if(maxCount==None or d>maxCount):
        maxCount=d
        maxPerson=k

print(maxPerson,maxCount)


