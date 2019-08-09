n,k=map(str,input().split())
a=len(n)
r=0
while(a>0):
  a=a-1
  if(n[a]==k):
    r=r+1
print(r)  
