# 0412
# 자료형 - 리스트, 튜플, 딕셔너리, 집합
# "김밥", "떡볶이", "돈까스"
'''
리스트
["김밥", "떡볶이", "돈까스"]
튜플 
("김밥", "떡볶이", "돈까스")

딕셔너리 - 사전 apple - 동그란 빨간 과일
{k1:v1 , k2:v2}
address = {"홍길동":"구로구", "김길동" : "부천", "박길동":"인천"}

json 형식 -
key:Value
'''
#["김밥", "떡볶이", "돈까스", "칼국수"]

#1. 빈 리스트를 만들어서, 하나씩 원소를 추가하는 방식

lst = []
print(type(lst))
lst.append("김밥")
lst.append("햄버거")
lst.append("감튀")
lst.append("탕수육")
#print(lst)
lst.append("파스타")
#print(lst)
lst.insert(0, "커피")
#print(lst)
lst.insert(0, "썹웨")
'''
#print(lst)

print("list에서 3번째에 있는 값입니다. : " , lst[2])
#점심메뉴출력하기 2
for i in range(len(lst)) :
    print(lst[i])

#점심메뉴출력하기 2
for item in lst :
    print(item)

print(lst)
print('lst.count("탕수육")', 'lst.index("탕수육"), ')

#slicing
['썹웨', '커피', '김밥', '햄버거', '감튀', '탕수육', '파스타', '탕수육', '탕수육', '탕수육']
#lst[start:end:step]
#lst[0,10,1] 0~(10-1), step 수 만큼 뛰어 넘어라.
print(lst[::])
print(lst[:len(lst):1])#전체 [0:11:1]
print(lst[0:8:2])#0~7 2칸씩 뛰어넘기['썹웨', '김밥', '감튀', '파스타']
print(lst[3:7:1])# 3~6['햄버거', '감튀', '탕수육', '파스타']
print(lst[::-1])#거꾸로
print(lst[0:6:3]) #0~5 3칸씩 0,3['썹웨', '햄버거']

#remove
lst.remove("김밥")
lst.remove("탕수육")
lst.append("커피")
print(lst)

item1="커피"
if item1 in lst :
    lst.remove(item1)
    print("커피존재함",lst)
else :
    print("커피존재안함", lst)

#pop
print(lst)
print("lst.pop():" , lst.pop())
print(lst)

print("lst.pop():" , lst.pop())
print(lst)

print("lst.pop():" , lst.pop(0))
print(lst)
'''
''''''''''
print(lst)
dessert = ["케잌", "커피", "우유", "와플"]
print(dessert)
lst.extend(dessert) #list+ list2 = list

print(lst)
#sort vs sorted
l1 = ["orange", "apple", "mango", "kiwi","banana"]
print(l1)
#l2 = sorted(l1)
#print(l2)
print(sorted(l1))
print(l1)

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.clear()
print(l1)

del l1
print(l1)
'''
#리스트 컴프리핸션
#리스트를 선언할때, 짧게, 빠르게 간결하게 하고싶다.
#0~10까지 숫자가 있는 리스트를 선언하라.
#1) 그냥 선언
l2 = [0,1,2,3,4,5,6,8,9,10]
print(l2)
#2)for 문으로 append
l3 = []
for i in range(11) :#0~10 , 0,1,2,3,4,5, ... , 10
    l3.append(i)
print(l3)

#3) 리스트 컴프리핸션
l4 = [ i for i in range(11)]
print("l4", l4)



#4)0-10까지의 숫자의 제곱을 리스트에 넣어라
#[0,1,4,9,...,81,100]
l5 = []
for i in range(11):
    l5.append(i**2)
    l5 = [i**2 for i in range(11)]
#5)0-10까지의 숫자의 3배수 리스트에 넣어라
#[0,3,6,9,...,30]
l6 = [i*3 for i in range(11)]
print(l6)
#6) hello를 10번 넣어라
#['hello','hello',....,'hello',]

l7 = []
for i in range(10) :
    l7.append("hello")

l7 = ["hello" for i in range(10)]

#7) 0~10까지 짝수들의 제곱을 리스트에 넣으시오.
#[0,4,16,36,84,100]
l8 = []
for i in range(11):
    if i % 2 == 0 :
        l8.append (i**2)
print(l8)

l9 = [ i**2 for i in range(11) if i % 2 == 0]
print(l9)


#list 를 복사
a= [0,4,16,36,64,100]
b=a
#c = a[:] #[:]
#c = a.copy()
c = list(a)
a.pop()
print(a)
print(b)
c.append("333")
#deep copy
print(a)
print(b)
print(c)

