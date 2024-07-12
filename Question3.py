'''
Question: With a given integral number n, write a program to generate a dictionary
that contains (i, i*i) such that is an integral number between 1 and n (both included).
and then the program should print the dictionary. Suppose the following input is supplied to the program: 8
Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''

n=int(input())

dict1={}

for i in range(1,n+1):
    dict1[i]=i*i


print(dict1)
#标准答案：
##dict() 函数用于创建一个字典。

'''
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
**kwargs -- 关键字。
mapping -- 元素的容器，映射类型（Mapping Types）是一种关联式的容器类型，它存储了对象与对象之间的映射关系。
iterable -- 可迭代对象。
'''
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)