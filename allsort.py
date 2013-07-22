'''
Created on 2013年7月22日
对一个数组进行全排列输出
@author: lin
'''
COUNT=0


def perm(num_list,begin,end):
    global COUNT
    if begin>=end:
        print("enter")
        for num in num_list:
            print(num),
        COUNT +=1
    else:
        i = begin
        for num in range(begin,end):
            num_list[num],num_list[i]=num_list[i],num_list[num]  #两个数进行交换 
            perm(num_list,begin+1,end)
            num_list[num],num_list[i]=num_list[i],num_list[num]
num_list=["1","2","3","4","5"]
perm(num_list,0,5)
print("Total: %s" % COUNT)
exit
