employ=[]
array=[]
array2=[]
array3=[]
s=[]
w=int(input("ENTER THE NO. OF EMPLOY:"))
for i in range(0,w):
    p=input("ENTER THE NAME:")
    array.append(p)
array.sort()
for j in range(0,w):
    r=int(input("ENTER THE AGE:"))
    array2.append(r)
array2.sort()
for k in range(0,w):
    t=int(input("ENTER THE SALARY:"))
    array3.append(t)
array3.sort()
employ=array+array2+array3
print(employ)
