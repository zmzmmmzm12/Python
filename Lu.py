from numpy import zeros, eye

#filename='test_data.txt'
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

if i==3:            
    #일단 3*3행렬만 생각
    for idx_i in range(i):
        for idx_j in range(i):
            if idx_i == 0:
                U[idx_i][idx_j]=Mat2[idx_i][idx_j]
            elif idx_i == 1:
                if idx_j==0:
                    L[idx_i][idx_j]=Mat2[idx_i][idx_j]/U[0][idx_j]
                elif idx_j==1:
                    U[idx_i][idx_j]=Mat2[idx_i][idx_j]-L[idx_i][0]*U[0][idx_j]
                else:
                    U[idx_i][idx_j]=Mat2[idx_i][idx_j]-L[idx_i][0]*U[0][idx_j]
            else:
                if idx_j==0:
                    L[idx_i][idx_j]=Mat2[idx_i][idx_j]/U[0][idx_j]
                elif idx_j==1:
                    L[idx_i][idx_j]=(Mat2[idx_i][idx_j]-L[idx_i][0]*U[0][idx_j])/U[1][idx_j]
                else:
                    U[idx_i][idx_j]=Mat2[idx_i][idx_j]-L[idx_i][0]*U[0][idx_j]-L[idx_i][1]*U[1][idx_j]

elif i==2:
    for idx_i in range(i):
        for idx_j in range(i):
            if idx_i == 0:
                U[idx_i][idx_j]=Mat2[idx_i][idx_j]
            elif idx_i == 1:
                if idx_j==0:
                    L[idx_i][idx_j]=Mat2[idx_i][idx_j]/U[0][idx_j]
                elif idx_j==1:
                    U[idx_i][idx_j]=Mat2[idx_i][idx_j]-L[idx_i][0]*U[0][idx_j]

for idx_i in range(i):
    for idx_j in range(i):
        if idx_i==idx_j:
            L[idx_i][idx_j]=1
        if(idx_i<idx_j):
            L[idx_i][idx_j]=0
        if(idx_i>idx_j):
            U[idx_i][idx_j]=0


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
y[0][0]=b[0][0]
y[1][0]=b[1][0]-L[1][0]*y[0][0]
if i==3:
    y[2][0]=b[2][0]-L[2][0]*y[0][0]-L[2][1]*y[1][0]

x=zeros((i,1))
if i==3:
    x[2][0]=y[2][0]/U[2][2]
    x[1][0]=(y[1][0]-U[1][2]*x[2][0])/U[1][1]
    x[0][0]=(y[0][0]-U[0][1]*x[1][0]-U[0][2]*x[2][0])/U[0][0]
elif i==2:
    x[1][0]=y[1][0]/U[1][1]
    x[0][0]=(y[0][0]-U[0][1]*x[1][0])/U[0][0]

print(x)
for k in range(i):
    out.write(str(x[k][0])) #구하고자 하는 해
    out.write("\n")

out.close()
