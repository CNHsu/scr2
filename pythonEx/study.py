N= int(input("how mabdy: "))
account={}
for i in range(N):
    account[i]=0
    i=i+1
T=int(input("action: "))
for i in range(T):
    transtr=input("transaton: ")
    transtr=transtr.split()
    trans=list(map(int,transtr))
    
    n=int(trans[0])
    t=int(trans[1])
    m=int(trans[2])
    print(n,t,m)
    if t ==1 or t==3:
        account[n]=account[n]+m
    elif t==2:
        account[n]=account[n]-m
    if t==4 and m==0:
        del account[n]
    print("account[",n,"]= ",account[n])
sum=0
for key,value in account.items():
    print(key,value)
    sum =sum + value
print("total =  ",sum)
        
        