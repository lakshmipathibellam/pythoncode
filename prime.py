n=int(input('enter a number :'))
d=2
cnt=0
while d<n//2:
    if n%d==0:
        cnt+=1
    d+=1
if cnt==0:
    print('prime')
else:
    print('not prime')
