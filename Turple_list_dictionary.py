'''
Created on 2013年7月14日

@author: lin
'''
print("This is first python")
print("%.f" % 12.33)
city = ("xi'an" , "fuzhou","beijing","anwei")  #这是一个元组，不可更改的数据序列
print(len(city)) 
print(city)

'''
下面是列表-可以更改的数据序列
'''
breakfast=["coffee","tea","toast","eggs"]
print(breakfast[0])
breakfast[1]="milk"
print("The breakfast[1]:%s" % breakfast[1])
print(breakfast[0][0])
print(breakfast[-1])   #在不知道数组的长度的情况下，快速访问列表的最后一位

'''
下面是字典，以名称索引的分组数据
'''
name={}
name["cityName"] = "fuzhou"
name["countryName"] = "china"

print(name)
print(name.keys())  #从字典中获取键值
print(list(name.values()))

name1={"city":"beijing","country":"american"}
print(name1)

