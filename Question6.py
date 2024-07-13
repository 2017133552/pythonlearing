'''
Question: Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]:
Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values
should be input to your program in a comma-separated sequence. Example Let us assume the
following comma separated input sequence is given to the program: 100,150,180
The output of the program should be: 18,22,24
'''
import math
C=50
H=30
d=map(int,input().split(","))
ans=[]
for item in d:
    ans.append(str(int(math.sqrt(2*C*item/H))))
#注意没有做到四舍五入
print(",".join(ans))

##参考答案：

import math
c=50
h=30
value=[]
item=[x for x in input().split(",")]

for d in item:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(",".join(value))