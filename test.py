def fn(arry,varb):
    arry[0][1]=1
    return arry,varb
b=[[0,0],[1,1]]
v=1
a,v = fn(b,v)
print a, b
