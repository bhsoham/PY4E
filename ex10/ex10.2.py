fname=input("Enter file name: ")
fhandle=open(fname)

hrs=list()
temp=list()
counts=dict()

for line in fhandle:
    if line.startswith("From "):
        words=line.split()
        time=words[5].split(":")
        hrs.append(time[0])

for hour in hrs:
    counts[hour]=counts.get(hour,0)+1

for k,v in counts.items():
    temp.append((k,v))

for k,v in sorted(temp):
    print(k,v)
