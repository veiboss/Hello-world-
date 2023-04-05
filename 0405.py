# 0405
# 문자열
'''
str = "파이썬수업 씨수업 자바수업 파이썬수업 파이썬수업"
str2 = "파이썬수업,씨수업,자바수업,이썬수업,파이썬수업"

#format
#3+4=7
print(3,"+",4,"=",7)
f = "{} + {} = {}".format(3,4,7)
f2 = "{0} + {1} = {2}, {2}, {2}, {2}".format(3,4,3+4)
f3 = "{0:d} + {1:f} = {2:f}, {2}, {2}, {2}".format(3,4.0,3+4.0)
f4 = "{0:10d} + {1:10f} = {2:10.3f}".format(3,4.0,3+4.0)
print(f4)

#join
#print("**".join(str))


#replace
print(str.replace("파이썬", "자바", 3))

#count
print(str.count("파이썬"))

#find, index
print ("find : ", str.find("씨"), "index : ", str.index("씨"))
print(str.find("AI"))
print(str.index("AI"))

#split
print(str.split())
print(str2.split(","))
print(str2.split("업"))
'''
'''
#bool
print(type(True), type(False))
a = "hello"
print(bool("hello"), bool("hi"), bool(3), bool(1.2), bool(-2))
print(bool(""), bool(0))
print(int(True), int(False), str(True))
'''

#조건문
'''
if 조건1 :
    실행문1 #참
elif 조건2 :
    실행문 2
    elif 조건10 :
    실행문 10
else :
    실행문3 #거짓
    
#오전 / 오후
h = 9
if h <12 :
    #h가 12보다 작을때
    print("오전", h, "가 12보다 작다")
elif h<18: #12<h<1i8
    print("오전", h, "가 12보다 크고 18보다 작아욧")

else : #18<h
    #실행문 2
    #h가 12보다 크다.
    print("오후", h, "는 18보다 크다.")

lunch = input("밥 먹을래?")
if lunch == "yes" :
    print("밥 묵자")
    cafeteria = input("학식?")
    if cafeteria == "yes" :
        print("8호관 ㄱ")
    else :
        print("역시 학식은 좀 글치?")
        subway = input("썹웨 어떠심?")
        if subway == "yes" :
            print("8호관 1층 바로가")
        else :
            print("썹웨가 싫다고?")
else :
    print("밥 먹지마!")
    '''
#for, while
# 반복문
'''
for i in 1,2,3,4,5,6 :
    print("i : ", i)

for i in range(20) :
    print("i :", i)'''
'''
#1부터 10까지 합을 구하시오.
#2가지 방법으로, range도 쓰고, 그냥 명시도 하고
sum = 0
for i in 1,2,3,4,5,6,7,8,9,10 :
    #sum = sum + i
    sum += i
    print(i ,' 번째 loop입니다. sum은' , sum, '입니다' )
else :
    print("else")'''
'''
sum = 0
n = 0 
while n< 11 :
    sum += n 
    print(n, end=" ")
    n = n+1

    print("while 밖에서 sum의 값 :", sum)
'''