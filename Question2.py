'''
Question: Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 5 6 8 20
Then, the output should be: 120,720,40320,2432902008176640000
'''
def factorial(n):
    if n==1:
        return 1
    else:
        return factorial(n-1)*n

num=list(map(int,input().split()))
ans=[]
for item in num:
    ans.append(str(factorial(item)))

print(",".join(ans))

