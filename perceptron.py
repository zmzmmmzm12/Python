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
        
def perceptron(test, training, cntTraining):
    #랜덤값으로 초기화(0~1)
    w1=random.random(); w2=random.random();w3=random.random();bias=random.random();
    print('random w:', w1,w2,w3,bias)
    #초기화된 값으로 test
    for idx_i, val_i in enumerate(test):
        x1=val_i[0]; x2=val_i[1]; x3=val_i[2]
        tmp=w1*x1+w2*x2+w3*x3+bias
        if tmp<=0:
            val_i[4]=0
        else:
            val_i[4]=1
    #perceptron실행
    for i in range(0,1000): #최대 1000번
        checkCnt=0
        for idx_i, val_i in enumerate(training):
            x1=val_i[0]; x2=val_i[1]; x3=val_i[2]; M=val_i[3]
            tmp=w1*x1+w2*x2+w3*x3+bias
            n=0.05 #학습률
            if M==0:
                if tmp>0:
                    if x1!=0:
                        w1=w1-x1/abs(x1)*n;
                    if x2!=0:
                        w2=w2-x2/abs(x2)*n;
                    if x3!=0:
                        w3=w3-x3/abs(x3)*n;
                    bias=bias-1*n
                else:
                    checkCnt=checkCnt+1
            else:
                if tmp<=0:
                    if x1!=0:
                        w1=w1+x1/abs(x1)*n;
                    if x2!=0:
                        w2=w2+x2/abs(x2)*n;
                    if x3!=0:
                        w3=w3+x3/abs(x3)*n;
                    bias=bias+1*n
                else:
                    checkCnt=checkCnt+1
            #print(tmp,M,w1,w2,w3,bias)
        if checkCnt==cntTraining:
            break;
    return w1,w2,w3,bias

w1,w2,w3,bias=perceptron(inpSyntheticTest, inpSyntheticTraining, cntSyntheticTraining) #synthetic데이터
#w1,w2,w3,bias=perceptron(inpRealTest, inpRealTraining, cntRealTraining) #real데이터
print('perceptron w:',w1,w2,w3,bias)
x0c=[]; y0c=[]; z0c=[] #training끝난 class0의 x,y,z값을 담을 부분
x1c=[]; y1c=[]; z1c=[] #training끝난 class1의 x,y,z값을 담을 부분

def perceptronTest(test, w1, w2, w3, bias):
    cntNoPerceptron0=0; cntNoPerceptron1=0;
    cntPerceptron0=0;cntPerceptron1=0;
    for idx_i, val_i in enumerate(test):
        x1=val_i[0]; x2=val_i[1]; x3=val_i[2]; M=val_i[3]
        tmp=w1*x1+w2*x2+w3*x3+bias
        if tmp<=0:
            val_i[5]=0
            x0c.append(val_i[0]); y0c.append(val_i[1]); z0c.append(val_i[2])
        else:
            val_i[5]=1
            x1c.append(val_i[0]); y1c.append(val_i[1]); z1c.append(val_i[2])
        #잘못 분류된 갯수 체크
        if M==0:
            if val_i[4]==1:
                cntNoPerceptron0=cntNoPerceptron0+1;
            if val_i[5]==1:
                cntPerceptron0=cntPerceptron0+1;
        if M==1:
            if val_i[4]==0:
                cntNoPerceptron1=cntNoPerceptron1+1;
            if val_i[5]==0:
                cntPerceptron1=cntPerceptron1+1;
    return cntNoPerceptron0,cntNoPerceptron1,cntPerceptron0,cntPerceptron1

cntNoPerceptron0,cntNoPerceptron1,cntPerceptron0,cntPerceptron1 = perceptronTest(inpSyntheticTest,w1,w2,w3,bias) #synthetic데이터
#cntNoPerceptron0,cntNoPerceptron1,cntPerceptron0,cntPerceptron1 = perceptronTest(inpRealTest,w1,w2,w3,bias) #real데이터
print(cntNoPerceptron0,cntNoPerceptron1,cntPerceptron0,cntPerceptron1)

def plotBinaryClassifiedData3D(x0, y0, z0, x1, y1, z1, color0="#ff2200", color1="#0077ff"):
    ax=plt.axes(projection='3d')
    ax.scatter(x0, y0, z0, c=color0, label="class0", marker='o', cmap='viridis', linewidth=0.5)
    ax.scatter(x1, y1, z1, c=color1, label="class1", marker='o', cmap='viridis', linewidth=0.5)
    ax.legend()
    
plotBinaryClassifiedData3D(x0c,y0c,z0c,x1c,y1c,z1c)
