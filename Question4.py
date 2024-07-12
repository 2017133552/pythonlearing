s=input().split(",")
print(s)
L=[]
T=()#tup1 = ();创建空元组
'''
元组中只包含一个元素时，需要在元素后面添加逗号
tup1 = (50,)
'''
for i in s:###字符串的 split() 方法用于根据指定的分隔符将字符串拆分成多个部分，并返回这些部分组成的列表。；所以不需要再用列表来存储了
    L.append(i)
    T+=(i,)
print(L)
print(T)
print(tuple(L))
'''
Python 元组 tuple() 函数将列表转换为元组。
tuple( iterable )
iterable -- 要转换为元组的可迭代序列。
'''