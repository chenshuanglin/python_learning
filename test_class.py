'''
Created on 2013年7月15日

@author: lin
'''


        

class Fridge:
    '''
    classdocs
    '''
    name="ffff"

    def __init__(self,name1):
        '''
        Constructor
        '''
        name=name1
        return
    def printSome(self,strString):
        if type(strString) != type(""):
            print("你输入的参数有误")
        else:   
            print(self.name)
        return
    
class test:
    b=Fridge("bejing");
    def __init__(self,a):
        b=a
    def print1(self):
        print(self.b.name)
c = Fridge("xian")
name=("shjian","fuzhou")
c.printSome("some")
c.printSome(name)
print(c.name)
test1 = test(c)
test.print1(test1)

 
        