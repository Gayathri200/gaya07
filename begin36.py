a=input()
w=['!','@','#','$','%','^','&','*','(',')','-','_','.']
b=len(w)
r=0
for i in range(0,b):
  if w[i] in a:
     r=r+1
print(r)     
