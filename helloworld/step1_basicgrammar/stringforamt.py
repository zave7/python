'''
Created on 2019. 6. 17.

@author: Administrator
'''
#문자열 포맷팅 해서 변수에 넣기
p = "이름 : %s님 안녕하세요!! %s입니다!!" % ("자바", "스프링")
print(p)

p = "X = %0.3f, Y = %-10.2f"  % (3.123, 3.14)
print(p) 
# str 문자열 클래스

s = "abd"
print("s = " + str(s))
print(type(s))
print(s[0])
