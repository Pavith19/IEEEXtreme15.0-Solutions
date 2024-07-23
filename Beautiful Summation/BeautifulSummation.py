"""
Author: Pavith Bambaravanage
URL: https://github.com/Pavith19
"""
def SN(p,q,n):
    if n==1:
        sn=p
        return (sn)
    else:
        return ((p**n)*(n**q))+ SN(p,q,n-1)

def ans(start,end,p,q):
    if (end+1)==0:
        sn=0
        return sn
    elif (end+1)==1:
        sn=p
        return sn
    elif end%2==0:
        return (p**(end+1)*(end+1)**q)+ans(start,end/2,p,q)+ans(end/2,end,p,q)
        
    else:
        return (p**(end+1)*(end+1)**q)+ans(start,end//2,p,q)+ans((end//2)+1,end,p,q)
        

def power(x, n, memo):
    if n in memo:
        return memo[n]
    else:
        # base condition
        if n == 0:
            return 1
    
        if n & 1:    # if `n` is odd
            memo[n] = x * power(x, n // 2, memo) * power(x, (n // 2), memo)
    
        # otherwise, `n` is even
        memo[n] = power(x, n // 2, memo) * power(x, (n // 2), memo)
    
    return memo[n]


P,Q,N,M = map(int,input().split())

SN=0
memo = {}
prev = 1
for k in range(1,N+1):
    new = prev * P
    SN = SN + new * power(k,Q, memo)
    prev = new

print(SN % M)


P,Q,N,M = map(int,input().split())
SN=0
for i in range(2,(N+1),2):
    SN=SN +((P**i-1)((i-1**Q)+(P*(i**Q))))
if N%2!=0:
    SN+=()
print(SN%M)
