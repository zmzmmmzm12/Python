from numpy import zeros
import sys

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

Mat2=zeros((i,i+1))

for idx_i, val_i in enumerate(Mat):
    for idx_j, val_j in enumerate(val_i):
        Mat2[idx_i][idx_j]=int(Mat[idx_i][idx_j])

def gauss(mat, i):
    idx_i = list(range(len(mat)))
    idx_j = len(mat[0])
    rmat=[]
    for c in range(i-1):
        max=mat[c][c] #해당하는 행의 (열)
        maxnum=c
        if max==0: #0으로 시작하면 0이아닌걸로 바꿔주기
            for r in range(c,i):
                if mat[r][c]!=0:
                    max=abs(mat[r][c])
                    maxnum=r
        if max==0:#열이 모두 0이면 실행종료
            print("실행불가능")
            sys.exit()
        for r in range(c,i): #해당 열의 가장 큰값 찾아줌
            if max<abs(mat[r][c]) and mat[r][c]!=0:
                maxnum=r
                max=abs(mat[r][c])
        pivot=maxnum
        tmp=zeros((1,i+1))
        for r in range(i+1):
            if c<=idx_j-2:
                tmp[0][r]=mat[c][r]
                mat[c][r]=mat[pivot][r]
                mat[pivot][r]=tmp[0][r]
        if c<i:
            pivot=c
            for r in range(i):
                if r > pivot:
                    mul=mat[r][c]/mat[pivot][c]
                    mat[r]=[i1-mul*i2 for i1,i2 in zip(mat[r],mat[pivot])]
   
    for r in idx_i:
        rmat.append(mat[r])
    return rmat

Mat2=gauss(Mat2, i)
Mat3=zeros((i,i+1))

for idx_i, val_i in enumerate(Mat2):
    for idx_j, val_j in enumerate(val_i):
        Mat3[idx_i][idx_j]=float(Mat2[idx_i][idx_j])

print(Mat3) #가우스 소거법 결과 행렬
for k in range(i):
    for l in range(i+1):
        out.write(str(Mat3[k][l]))
        out.write("     ")
    out.write("\n")
out.write("\n") #결과값과 구분해주기

Mat4=zeros((i,i))
b=zeros((i,1))
for idx_i, val_i in enumerate(Mat):
    for idx_j, val_j in enumerate(val_i):
        if idx_j == i:
            b[idx_i][0]=Mat3[idx_i][idx_j]
        else:
            Mat4[idx_i][idx_j]=Mat3[idx_i][idx_j]

x=zeros((i,1)) #결과값 저장할 배열

def re(b, Mat4, x, i, k):
    ret=0
    for h in range(i-1, k, -1):
        ret = ret+x[h]*Mat4[k][h]
    return ret

for k in range(i-1,-1,-1): #3 기준 k는 2,1,0
    if k==i-1:
        x[k][0]=b[k][0]/Mat4[k][k]
    else:
        x[k][0]=(b[k][0]-re(b,Mat4,x,i,k))/Mat4[k][k]
        
print(x)
for k in range(i):
    out.write(str(x[k][0])) #구하고자 하는 해
    out.write("\n")
    
out.close()
