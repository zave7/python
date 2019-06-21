'''
Created on 2019. 6. 19.

@author: Administrator
'''
#text = b"Hello"
#for c in text:
#    print(c)
    
s1 = "A\u00e5"
print(s1)

b = s1.encode('utf-8')
print(b)
s2 = b.decode('utf-8')
print(s2)
