'''
Created on 2013年7月17日
该程序是递归修改目录下文件所有的扩展名
@author: lin
'''

import os

'''
其中path是所在文件的路径，before_ext，是要改之前的扩展名，ext是想要更改成的扩展名
'''
def model_extentsion(path,before_ext,ext):  
    for name in os.listdir(path):
        full_path=os.path.join(path,name)               #得到文件的完整的路径
        if os.path.isfile(full_path):                   #判断是否是一般文件
            split_path=os.path.splitext(full_path)      #对完整的路径名进行划分，得到扩展名，扩展名格式“.jpg”等
            pwd_name=split_path[0]                      #获得没有扩展名的文件名
            pwd_ext=split_path[1]                       #获得扩展名
            before_ext1="."+before_ext
            if pwd_ext == before_ext1:                 #判断文件的扩展名是否是要求修改的扩展名
                ext1="."+ext
                pwd_name+=ext1
                re_name=os.path.join(path,pwd_name)
                os.renames(full_path, re_name)           #重命名
          
            
        else:
            model_extentsion(full_path,before_ext,ext)    #如果是目录，递归进入目录

model_extentsion("/home/lin/test_jsp",'html', "jsp")
            
        
    


    

