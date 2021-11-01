from numpy import zeros
import random
import matplotlib.pyplot as plt

#파일열기(synthetic_training)
filenameSyntheticTraining='C:/Users\82107/Desktop/4학년 1학기/인공지능/인공지능_과제1설명/data/synthetic_data_train.txt'
with open(filenameSyntheticTraining, encoding='ascii') as file_objectSyntheticTraining:
    linesSyntheticTraining=file_objectSyntheticTraining.readlines()

cntSyntheticTraining=len(linesSyntheticTraining)
inpSyntheticTraining=zeros((cntSyntheticTraining, 4))

#한줄마다 ','기준으로 자르기
for line in range(0,cntSyntheticTraining):
    linesSyntheticTraining[line]=linesSyntheticTraining[line].strip().split(',')

#잘린 문자들을 float타입으로 변환해 배열에 넣기
for idx_i, val_i in enumerate(linesSyntheticTraining):
    for idx_j, val_j in enumerate(val_i):
        inpSyntheticTraining[idx_i][idx_j]=float(linesSyntheticTraining[idx_i][idx_j])
            
        
#파일열기(synthetic_test)
filenameSyntheticTest='C:/Users\82107/Desktop/4학년 1학기/인공지능/인공지능_과제1설명/data/synthetic_data_test.txt'
with open(filenameSyntheticTest, encoding='ascii') as file_objectSyntheticTest:
    linesSyntheticTest=file_objectSyntheticTest.readlines()
    
cntSyntheticTest=len(linesSyntheticTest)
inpSyntheticTest=zeros((cntSyntheticTest, 6))

#한줄마다 ','기준으로 자르기
for line in range(0,cntSyntheticTest):
    linesSyntheticTest[line]=linesSyntheticTest[line].strip().split(',')


#잘린 문자들을 float타입으로 변환해 배열에 넣기
for idx_i, val_i in enumerate(linesSyntheticTest):
    for idx_j, val_j in enumerate(val_i):
        inpSyntheticTest[idx_i][idx_j]=float(linesSyntheticTest[idx_i][idx_j])
        
#파일열기(real_training)
filenameRealTraining='C:/Users\82107/Desktop/4학년 1학기/인공지능/인공지능_과제1설명/data/datatraining.txt'
with open(filenameRealTraining, encoding='ascii') as file_objectRealTraining:
    linesRealTraining=file_objectRealTraining.readlines()

cntRealTraining=len(linesRealTraining)
inpRealTraining=zeros((cntRealTraining, 4))

#한줄마다 ','기준으로 자르기
for line in range(0,cntRealTraining):
    linesRealTraining[line]=linesRealTraining[line].strip().split(',')

#잘린 문자들을 float타입으로 변환해 배열에 넣기
for idx_i, val_i in enumerate(linesRealTraining):
    if idx_i != 0:
        inpRealTraining[idx_i-1][0]=float(linesRealTraining[idx_i][2])
        inpRealTraining[idx_i-1][1]=float(linesRealTraining[idx_i][4])
        inpRealTraining[idx_i-1][2]=float(linesRealTraining[idx_i][5])
        inpRealTraining[idx_i-1][3]=float(linesRealTraining[idx_i][7])    
            
#파일열기(real_test)
filenameRealTest='C:/Users\82107/Desktop/4학년 1학기/인공지능/인공지능_과제1설명/data/datatest2.txt'
with open(filenameRealTest, encoding='ascii') as file_objectRealTest:
    linesRealTest=file_objectRealTest.readlines()
    
cntRealTest=len(linesRealTest)
inpRealTest=zeros((cntRealTest, 6))

#한줄마다 ','기준으로 자르기
for line in range(0,cntRealTest):
    linesRealTest[line]=linesRealTest[line].strip().split(',')

#잘린 문자들을 float타입으로 변환해 배열에 넣기
for idx_i, val_i in enumerate(linesRealTest):
    if idx_i != 0:
        inpRealTest[idx_i-1][0]=float(linesRealTest[idx_i][2])
        inpRealTest[idx_i-1][1]=float(linesRealTest[idx_i][4])
        inpRealTest[idx_i-1][2]=float(linesRealTest[idx_i][5])
        inpRealTest[idx_i-1][3]=float(linesRealTest[idx_i][7]) 
        
x0c=[]; y0c=[]; z0c=[] #training끝난 class0의 x,y,z값을 담을 부분
x1c=[]; y1c=[]; z1c=[] #training끝난 class1의 x,y,z값을 담을 부분
def knn(training, test, k):
    cntMiss0=0; cntMiss1=0
    for idx_i, val_i in enumerate(test):
        x1=val_i[0]; x2=val_i[1]; x3=val_i[2];
        min=zeros((k,2)) #값과 클래스를 k개만큼
        for idx_j, val_j in enumerate(training):
            jx1=val_j[0]; jx2=val_j[1]; jx3=val_j[2]; jm=val_j[3]
            d=(x1-jx1)*(x1-jx1)+(x2-jx2)*(x2-jx2)+(x3-jx3)*(x3-jx3) #거리는 Euclidean distance의 제곱 사용
            if idx_j<k: #처음에 min에 암거도 없을때는 값 넣어주기
                min[idx_j][0]=d
                min[idx_j][1]=jm
            else:
                max=zeros((1,2))
                max[0][0]=0; max[0][1]=0 #필요한가 이게?
                for i in range(0,k):
                    if max[0][1]<min[i][0]: #max값은 min배열에서 가장 큰값(d랑 비교할값임)
                        max[0][0]=i; max[0][1]=min[i][0] #번호와 값
                if max[0][1] > d: #비교해보고 d가 더 작으면 값 바꿔넣기
                    min[int(max[0][0])][0]=d #거리
                    min[int(max[0][0])][1]=jm #클래스
        #training다돌고나면 k개로 체크
        cnt0=0; cnt1=0;
        for i in range(0,k):
            if min[i][1]==0:
                cnt0=cnt0+1
            else:
                cnt1=cnt1+1
        if cnt1>cnt0:
            val_i[4]=1
            x1c.append(val_i[0]); y1c.append(val_i[1]); z1c.append(val_i[2])
            if val_i[3]==0:
                cntMiss0=cntMiss0+1
        else: #cn1==cnt0일때도 클래스0으로 체크해줌
            val_i[4]=0
            x0c.append(val_i[0]); y0c.append(val_i[1]); z0c.append(val_i[2])
            if val_i[3]==1:
                cntMiss1=cntMiss1+1
    return cntMiss1, cntMiss0

#cntMiss1, cntMiss0=knn(inpSyntheticTraining,inpSyntheticTest,10) #synthetic
cntMiss1, cntMiss0=knn(inpRealTraining,inpRealTest,10) #real
print(cntMiss0, cntMiss1)

def plotBinaryClassifiedData3D(x0, y0, z0, x1, y1, z1, color0="#ff2200", color1="#0077ff"):
    ax=plt.axes(projection='3d')
    ax.scatter(x0, y0, z0, c=color0, label="class0", marker='o', cmap='viridis', linewidth=0.5)
    ax.scatter(x1, y1, z1, c=color1, label="class1", marker='o', cmap='viridis', linewidth=0.5)
    ax.legend()
    
plotBinaryClassifiedData3D(x0c,y0c,z0c,x1c,y1c,z1c)
