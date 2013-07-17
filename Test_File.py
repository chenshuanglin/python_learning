'''
Created on 2013年7月17日

@author: lin
'''
def make_text_file():
    a = open('/home/lin/python_learning/test.txt','w')
    a.write("This is create a new text file by python")
    a.close()
make_text_file()