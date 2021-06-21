#---
list1=[1,2,3,2,4,5,7,6,8,9]
result=[]
for i in list1:
    result.append(i+2)
    print(result)

#------
    
print("\n******************\n")




#------
for i in range(5,0,-1):
  for j in range(i,0,-1):
      print(j,end='')
  print()  

#--------

def fibonacci(n):
    if n<0:
     print("incorrect input")
    elif n==0:
      return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
    print(fibonacci(9))
#-----
num=int(input("enter the number"))
sum = 0
temp = num
while temp>0:
        digit=temp%10;
        sum +=digit**3
        temp//=10

        if num==sum:
            print(num,"is an armstrong number")
        else:
            print(num,"is not a armstrong number")

#-------
for i in range(1,11):
    print("9X",i,'=',i*9)

#--------
list1=[1,2,3,-1,-2,4,5,-6]
for i in list1:
    if i >=0:
        print(i,'is positive')
    else:
        print(i,'is negative')
            
            
#---------

def find(number_of_days):
    year=int(number_of_days/365)
    print(year,'year ago!')
#-----------

import math
def trigo(n,m):
    if n=='sin':
        return math.sin(m)
    elif n=='cos':
        return math.cos(m)
    elif n=='cosin':
        return math.cosin(m)
    elif n=='tan':
        return math.tan(m)
    elif n=='sec':
        return math.sec(m)
    elif n=='cosec':
        return math.cosec(m)
#-----------

def calculation():
    print('+')
    print('-')
    print('*')
    print('/')
    print('**')
    print('%')
    operation=input("select an operation:n")
    print("enter two number")
    number_1=int(input())
    number_2=int(input())

    if operation =='+':
        print(number_1 + number_2)
    elif operation =='-':
        print(number_1 - number_2)
    elif operation =='*':
        print(number_1 * number_2)
    elif operation =='/':
        print(number_1 / number_2)
    elif operation =='**':
        print(number_1 ** number_2)
    elif operation =='%':
        print(number_1 % number_2)
    else:
        print("invalid operation")
    
