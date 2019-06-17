'''
Created on 2019. 6. 17.

@author: Administrator
'''
#1.산술 연산자
print(5 % 2)
print(5 // 2)
print(5 / 2)
#2.비교 연산자 자바랑 거의 비슷
#==, !=, <, >, <=, >=
a = 5
if a != 1 :
    print("a는 1이 아님!!")
#3.할당 연산자 자바랑 거의 비슷
# +=, -=, *=, /=, %=
a = a * 10
a *= 10
print(a)
#4.논리 연산자
# and, or, not
x = True
y = False
if x and not y or True:
    print("yes")
else :
    print("No")
#5.비트 연산자
# &, |, ^, ~, <<, >>
b = 2
c = 3
print(b << 8)
#6.멤버쉽 연산자
a = [1,2,3,4]
b = 1.2 in a
if b:
    print("a 배열에 1이 속해있습니다")
else:
    print("a 배열에는 1.2가 속해있지 않습니다")
#7.Identify 연산자
# is 아무래도 객체의 값을 비교해서 보여주는듯..
aa = 1
bb = aa
if aa is bb :
    print("a 와 b는 같은 객체입니다")
else :
    print("a 와 b는 다른 객체입니다")