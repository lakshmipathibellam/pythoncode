s=[1,2,2,3,4,5,5,6,7,8,8,8]
#l=list(set(s))
#print(l)
l=[]
for i in s:
    if i not in l:
        l.append(i)
print(l)