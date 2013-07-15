'''
Created on 2013年7月14日
该程序主要是关于序列的一些操作
@author: lin
'''

'''
该程序片段主要是为了练习将序列切片
'''
slice_me=("the","next","time","we","meet","drinks","are","on","me")
slice_turple=slice_me[5:9]
print(slice_turple)

'''
该程序片段主要是为了练习将一个序列附加到另一个序列的末端
'''
living_room=("rug","table","chair","TV","dustbin")
apartment=["shijian"]
apartment.append(living_room)  #这段程序并没有把序列附加到另一个序列的末端,这只是增加了一个分层序列
print(apartment)

#用extend方法来进性插入
apartment1=[]
apartment1.extend(living_room)
print(apartment1)

'''
该程序片段主要是为了练习列表临时存储数据
'''
todays_temperatures = [23,32,33,31]
todays_temperatures.append(29)
print(todays_temperatures)

morning=todays_temperatures.pop(0)
print("This morning temperature was %.02f" % morning)

late_morning=todays_temperatures.pop(1)
print("Today late morning temperature was %.02f" % late_morning)

'''
该程序片段主要是为了练习集合
'''
city=["xian","fuzhou","beijing","xian"]
print(city)
city1=set(city)
print(city1)


