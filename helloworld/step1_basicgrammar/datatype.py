'''
Created on 2019. 6. 17.

@author: Administrator
'''
print("int(3.5) = " + str(int(3.5)))
print("2e3 = " + str(2e3))
print("float(\"1.6\") = " + str(float("1.6")))
print("float(\"inf\") = " + str(float("inf")))
print("float(\"-inf\") = " + str(float("-inf")))
print("bool(0) = " + str(bool(0)))
print("bool(-1) = " + str(bool(-1)))
print("bool(\"False\") = " + str(bool("False")))
a = None
a is None
if a is None :
    print("a는 None 입니다")