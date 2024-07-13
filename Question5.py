'''
Question: Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''
class Strclass(object):
    def __init__(self):#Hints: Use init method to construct some parameters
         self.s=""
        #'''错误预防：如果不在 __init__ 中初始化属性，而是在其他方法如 getString 中首次定义，
       # 那么在调用 printString 之前如果没有调用 getString，
        #就会遇到 AttributeError，因为 input_string 属性在尝试访问时尚未存在。'''
    def getString(self):
        self.s=input()

    def  printString(self):
        print(self.s.upper())
        '''
        描述
Python upper() 方法将字符串中的小写字母转为大写字母。

语法
upper()方法语法：

str.upper()
参数
NA。
返回值
返回小写字母转为大写字母的字符串。空格不变，其他字符不变仍然会保留。
        '''
#简单的测试函数来测试类方法
str1=Strclass()
str1.getString()
str1.printString()
