#import random

#print(random.randint(0,10000))

from random import randint
#from random2 import randint
print(randint(0,10000))





#놀이동산 탑승 문제
# 총 정원 4명
#정원이 차면, 놀이기구 시작
#조건 키 150 이상만 탈 수 있음.
# 사람들한테 키를 물어보고, 탑승시키시오.
#150이상 4명이 되면 놀이기구 시작
n=0
sum =0 

while n < 4 :
    height = int(input("키가 얼마세요?"))
    sum += n
    if height >= 150 :

        print("탑승 가능하세요" )
        n = n+1
    else :
        print("좀더 커서 오세요")
print("놀이기구 시작할게요!")