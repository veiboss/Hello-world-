#0329sss
'''
print ("안녕하세요.")
print (3)
print(10.6)

var = "안녕"
print(var)
print(type(var))
print(type(3))

var1 = 3
_var = 10
height = 180
weight = 50
length_list = 23
'''


#c=a+b
#a=c
#a=a+b
#a += b
#a <- a*b
'''
a,b=100,10
a=b
print("a :", a)
a,b=100,10
a+=b
print("a :", a)
a,b=100,10
a-=b
print("a :", a)
a,b=100,10
a*=b
print("a :", a)
a,b=100,10
a/=b
print("a :", a)
a,b=100,10
a%=b
print("a :", a)
a,b=100,10
a//=b
print("a :", a)
a,b=100,10
a**=b
print("a :", a)
'''

#name = input("이름이 뭔가요?")
#print("제 이름은", name, "입니다.")
#age = input("나이는?")
#print("나이는", age, "입니다.") # "20", int ("20")
#print("아버지 나이는", int(age)+30, "입니다.")
#print(type(age))

#int("30")
#float("20.6")
#str(30)
'''planet = input('원하는 행성은?')
strRadius = input(planet + '반지름은?')
radius = int(strRadius)

length = 2*3.14*radius
print(planet, '반지름 :', radius)
print(planet, '둘레길이:', length)'''

#a = 'python'
'''a= '동양미래대학교'
print(a[0], a[1], '...', a[5])
print('python'[0], "...", 'python'[1], '...', 'python'[5])
print('동양미래대학교'[0])
print(len(a))'''

'''school = '동양미래대학교-컴퓨터소프트웨어공학과'
print("school[::-1]", school[::-1])#동양미래대
print('school[0:len(school):2]', school[0:len(school):3])#동미대교컴...
print("school[8:len(school):2]", school[8:len(school):2])#양미래
print("school[8:len(school):]", school[8:len(school):])#미래
print("school[:15:4]", school[:15:4])'''
'''
print('python'[5:0:-1])
print('python'[-1:-7:-1])
#log 2023-3-20 20:20:20 222 error

print("hello \n world")
print("hello \t world")
print("hello\bworld")
print("hello\vworld")'''
'''
str_a="하하하"
#str_b="ghghghghg"
print(type(str_a))
print(str_a.replace ("하", "호"))
str_a = str_a.replace ("하", "호",1)
print("str_a :", str_a)
#print("str_b: ", str_b)
str_c = "안녕하세요. 파이썬 수업입니다. 파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬.파이썬."
print(str_c.replace("파이썬", "자바", 5))'''

n = (input("6자리 실수 입력 : "))
n = n.replace(".","")
print("sum : ",int(n[0])+int(n[1])+int(n[2])+int(n[3])+int(n[4])+int(n[5]))
