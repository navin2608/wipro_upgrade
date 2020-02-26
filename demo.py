a=int(input())
d1=[]
while(a>0):
    b=int(input())
    c=list(map(int,input().split()))
    su=sum(c)
    d=[]
    for j in c:
        d.append(su-j)
    a=a-1
    d1.append(d)
for i in d1:
    print(" ".join(str(j) for j in i))
