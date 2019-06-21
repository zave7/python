'''
Created on 2019. 6. 19.

@author: Administrator
'''
a = ["1", 5, False]
for i in a:
    print(i)
    
print(a[0])

#리스트 슬라이싱
a = [1, 2, 3, 4]
x = a[1:3]
print(x)
x = a[:3]
print(x)
x = a[3:]
print(x)

a = ["ab", 1, False]
a.append("1234")
a[2] = True 
del a[0]
print(a)

b = [1,2,3,4]
c = [5,6,7,8]
d = b + c
d = c + b
print(d)
#index 와 count
mylist = "this is apple !!".split()
i = mylist.index("this")
n = mylist.count("!!")
print(i)
print(n)
