'''
Created on 2013年7月17日
用递归的方法，将一个完整路径完全分解为若干目录的名称
@author: lin
'''
import os.path
def split_fully(path):
    parent_path, name=os.path.split(path)
    if name == "":
        return (parent_path,)
    else:
        return split_fully(parent_path)+(name,)
path="/home/lin/python_learning"
full_path=split_fully(path)
print(type(full_path))
print(full_path)

######一下是测试列出某个目录的所有内容##################
def print_dir(dir_path):
    for name in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path,name)):
            name=os.path.join(dir_path,name)
            print_dir(name)
        else:
            print(os.path.join(dir_path,name))
        
print("以下是打印某个目录下的内容")
print_dir("/home/lin")
