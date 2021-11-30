code=input()
codelist=[]
newcodelist=[]
psw=[]
for bit in code:
    codelist.append(int(bit))

for bit1 in range(len(codelist)-1):
    newcodelist.append(codelist[bit1]-codelist[bit1+1])
for i in newcodelist:
    if i==0:
        psw.append(0)
    else:
        psw.append(1)
k=psw[::-1]
if codelist[0]==1:
    k.append(1)
    
else:
    k.append(0)
for i in k[::-1]:
    print(i,end="")
