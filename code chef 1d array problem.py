a=int(input("no of test cases \n"))
d=[]
while(a>0):
    
    b=int(input("Enter the length"))
    c=list(map(int,input().split()))
    su=sum(c)
    for j in c:
        print(su-j,end=" ")
    a=a-1
        
        
