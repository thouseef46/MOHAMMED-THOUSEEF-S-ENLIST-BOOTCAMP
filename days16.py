#lambda
r = lambda x, y : x * y
print(r(10, 4))

#-----
from functools import reduce
  
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
  
print(fib(11))

#-----
nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

#--------------
list1=[2,4,5,6,7,8,9,21,12,14,15,27,36,81]
print(list1)
list2=list(map(lambda j:j%9==0,list1))
print("Result")
print(' '.join(map(str,list2)))
list2=list(filter(lambda j:j%9==0,list1))
print("Result")
print(' '.join(map(str,list2)))

#------
list1=[2,4,5,6,7,8,9,21,12,14,15,27,36,81]
print(list1)
list2=list(filter(lambda j:j%2==0,list1))
print("Result :")
print(len(list2))
