#请编写一个函数输入n, 输出n个斐波那契数列的列表。 如：fib(5) -> [1, 1, 2, 3, 5]
def fib(x) :  
      if   x<=2:
           return 1
      else:
           return fib(x-1)+fib(x-2)


n=int(input())
for i in range (1,n+1):
       print(fib(i),'\t', end="")