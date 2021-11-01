from ImgProcessing import ImgProcessing
from PIL import Image
import numpy as np

if __name__ == '__main__':
    imgCsv00 = np.array(Image.open("./Lena_00c.png"))/255.0 #이미지가 csv형태로 열림
    imgCsv40 = np.array(Image.open("./Lena_40c.png"))/255.0
    imgCsv60 = np.array(Image.open("./Lena_60c.png"))/255.0


    k = 64
    p00 = np.random.normal(0, 1 / k, size=(256, k)) #랜덤으로 배열 생성
    q00 = np.random.normal(0, 1 / k, size=(k, 256))

    p40 = np.random.normal(0, 1/k, size=(256, k))
    q40 = np.random.normal(0, 1 / k, size=(k, 256))

    p60 = np.random.normal(0, 1 / k, size=(256, k))
    q60 = np.random.normal(0, 1 / k, size=(k, 256))

    a= 0.1 #Learning rate
    breakPoint=0.5 #epsilon
    lamda=0.0
    prevL00=0 #l을 체크하기 위해 previousL을 만들어줌
    prevL40=0
    prevL60=0
    for e in range(100):
        global current
        l00=0 #l=0으로 시작
        l40=0
        l60=0

        #imgCsv00에 대한 부분
        # for i in range(256):
        #     for j in range(256):
        #         if imgCsv00[i][j]>0: #만약 값이 있으면
        #             res=0
        #             for k2 in range(k):
        #                 res += p00[i][k2] * q00[k2][j] #스칼라곱을 해주려고
        #             for k2 in range(k):
        #                 p00[i][k2] = p00[i][k2] + a * ((imgCsv00[i][j] - res) * q00[k2][j] - lamda * p00[i][k2]) #p업데이트
        #                 q00[k2][j] = q00[k2][j] + a * ((imgCsv00[i][j] - res) * p00[i][k2] - lamda * q00[k2][j]) #q업데이트
        # 브레이크 포인트 결정
        # for i in range(256):
        #     for j in range(256):
        #         if imgCsv00[i][j] > 0:
        #             res = 0
        #             p = 0
        #             q = 0
        #             for k2 in range(k):
        #                 res += p00[i][k2] * q00[k2][j]
        #                 p += (p00[i][k2]*p00[i][k2])
        #                 q += (q00[k2][j]*q00[k2][j])
        #             l00 += ((imgCsv00[i][j] - res) * (imgCsv00[i][j] - res) + lamda * (p*p) + lamda * (q*q)) #l값 계산
        #
        # print(e, abs(l00 - prevL00)) #몇번돌았는지, 차이가 얼만지 테스트
        # if abs(l00 - prevL00) < breakPoint: #만약 차이가 breakPoint보다 낮으면 반복 종료
        #     break
        # prevL00=l00 #차이가 breakPoint보다 크면 prevL에 현재 l값을 넣어줌


        #imgCsv40에 대한 부분
        l40=0
        for i in range(256):
            for j in range(256):
                if imgCsv40[i][j]>0:
                    res=0
                    for k2 in range(k):
                        res += p40[i][k2] * q40[k2][j]
                    for k2 in range(k):
                        p40[i][k2] = p40[i][k2] + a * ((imgCsv40[i][j] - res) * q40[k2][j] - lamda * p40[i][k2])
                        q40[k2][j] = q40[k2][j] + a * ((imgCsv40[i][j] - res) * p40[i][k2] - lamda * q40[k2][j])

        for i in range(256):
            for j in range(256):
                res = 0
                p = 0
                q = 0
                for k2 in range(k):
                    res += p40[i][k2] * q40[k2][j]
                    p += (p40[i][k2] * p40[i][k2])
                    q += (q40[k2][j] * q40[k2][j])
                l40 += ((imgCsv40[i][j] - res) * (imgCsv40[i][j] - res) + lamda * p *p + lamda * q*q)  # l값 계산
        print(e, abs(l40 - prevL40)) #몇번돌았는지, 차이가 얼만지 테스트
        if abs(l40 - prevL40) < breakPoint: #만약 차이가 breakPoint보다 낮으면 반복 종료
            break
        prevL40=l40

        #imgCsv60에 대한 부분
        # l60=0
        # for i in range(256):
        #     for j in range(256):
        #         if imgCsv60[i][j] > 0:
        #             res = 0
        #             for k2 in range(k):
        #                 res += p60[i][k2] * q60[k2][j]
        #             for k2 in range(k):
        #                 p60[i][k2] = p60[i][k2] + a * ((imgCsv60[i][j] - res) * q60[k2][j] - lamda * p60[i][k2])
        #                 q60[k2][j] = q60[k2][j] + a * ((imgCsv60[i][j] - res) * p60[i][k2] - lamda * q60[k2][j])
        #
        # for i in range(256):
        #     for j in range(256):
        #         res = 0
        #         p = 0
        #         q = 0
        #         for k2 in range(k):
        #             res += p60[i][k2] * q60[k2][j]
        #             p += (p60[i][k2] * p60[i][k2])
        #             q += (q60[k2][j] * q60[k2][j])
        #         l60 += ((imgCsv60[i][j] - res) * (imgCsv60[i][j] - res) + lamda * p *p + lamda * q*q)  # l값 계산
        #
        # print(e, abs(l60 - prevL60))  # 몇번돌았는지, 차이가 얼만지 테스트
        # if abs(l60 - prevL60) < breakPoint:  # 만약 차이가 breakPoint보다 낮으면 반복 종료
        #     break
        # prevL60 = l60

    # current00 = p00 @ q00  # 업데이트 완료. 00에 대한 결과
    # print(imgCsv00*255)
    # current00 = current00 * 255
    # current00=current00.astype(int)
    # print(current00)
    # corruption_rate = 0.0
    # ImgProcessing.print_img_list(imgCsv00, imgCsv00, current00, corruption_rate)

    current = p40 @ q40 #40에 대한 결과
    current=current * 255
    current=current.astype(int)
    ImgProcessing.print_img(current)
    corruption_rate = 40.0
    ImgProcessing.print_img_list(imgCsv00, imgCsv40, current, corruption_rate)

    # current2=p60@q60 #60에 대한 결과
    # current2=current2*255
    # current2=current2.astype(int)
    # ImgProcessing.print_img(current2)
    # corruption_rate = 60.0
    # ImgProcessing.print_img_list(imgCsv00, imgCsv60, current2, corruption_rate)
