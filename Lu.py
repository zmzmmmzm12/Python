from numpy import zeros, eye

filename='input.txt'
with open(filename, encoding='ascii') as file_object:
    lines = file_object.readlines()

out=open(r'C:\Users\pc\Desktop\3-1\수치해석/output.txt','w')
Mat=[]

for line in lines:
    Mat.append(line.split())

i=0
for k in enumerate(Mat):
    i=i+1

Mat2=zeros((i,i))
b=zeros((i,1))
L=zeros((i,i))
U=zeros((i,i))

for idx_i, val_i in enumerate(Mat):
    for idx_j, val_j in enumerate(val_i):
        if idx_j==i:
            b[idx_i][0]=int(Mat[idx_i][idx_j])
        else:
            Mat2[idx_i][idx_j]=int(Mat[idx_i][idx_j])

for idx_i in range(i):
    for idx_j in range(i):
        U[idx_i][idx_j]=Mat2[idx_i][idx_j]
        if(idx_i==idx_j):
            L[idx_i][idx_j]=1
            
for idx_i in range(i):
    for idx_j in range(idx_i+1, i):
        L[idx_j][idx_i]=U[idx_j][idx_i]/U[idx_i][idx_i]
        for idx_k in range(i):
            U[idx_j][idx_k] -= (L[idx_j][idx_i]*U[idx_i][idx_k])

print(L)
print(U)

for k in range(i):
    for l in range(i):
        out.write(str(L[k][l]))
        out.write("     ")
    out.write("\n")
out.write("\n")

for k in range(i):
    for l in range(i):
        out.write(str(U[k][l]))
        out.write("     ")
    out.write("\n")
out.write("\n")

y=zeros((i,1))

def re(L, y, i, k):
    ret=0
    for h in range(k):
        ret += (L[k][h]*y[h][0])
    return ret

for k in range(i):
    if k==0:
        y[k][0]=b[k][0]
    else:
        y[k][0]=b[k][0]-re(L,y,i,k)

x=zeros((i,1))

def re2(U, x, i, k):
    ret=0
    for h in range(i-1, k, -1):
        ret = ret+x[h]*U[k][h]
    return ret

for k in range(i-1,-1,-1): #3 기준 k는 2,1,0
    if k==i-1:
        x[k][0]=y[k][0]/U[k][k]
    else:
        x[k][0]=(y[k][0]-re2(U,x,i,k))/U[k][k]

print(x)
        
for k in range(i):
    out.write(str(x[k][0])) #구하고자 하는 해
    out.write("\n")

out.close()
