'''
Created on 2019. 6. 17.

@author: Administrator
'''
s = ','.join(['가나', '다라', '마바'])#스트링 배열
print(s)

items = s.split(",");
print(items)

s = ''.join(['가나', '다라', '마바'])
print(s)

s1, s2, s3 = "test-str".partition("-")
print(s1)
print(s2)
print(s3)

#s = "Name : {0}, Age : {1} ".format("테스트", 20)
str = "Name : {0}, Age : {1} ";
p = str.format("asd", "23")
print(str.format("asd", "23"))











