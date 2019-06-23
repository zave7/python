'''
Created on 2019. 6. 19.

@author: Administrator
'''
class my_object:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printf(self):
        print('test')
my = my_object(1, 2)
my.printf()