#error type
#name error
list=22
print(list1)

#type error
a='123'
a+=123

l=[1,2,3,4,6,7]
for i in range(2,1):
    print(i+1)

#syntax error

for i range(1,10):
    print(i)

in=123

#index error
l=[1,2,3,4,5,6,7]
for i in range(len(1)):
    print(1(i+1))


#module not found error

import modulexyz

#key error

dict1=dict()
dict1={1,2,3,4}
print(dict[123)
#value error

int("abc")

#zero division error

100/0
#--------------------

def caculator():
    try:
        print('+')
        print('-')
        print('*')
        print('/')
        print('%')
        print('**')
        operation=input("select an operation")
        print("enter two number")
        number_1=int(input())
        number_2=int(input())
        if operation=='+':
            print(number_1+number_2)
        elif operation=='-':
            print(number_1-number_2)
        elif operation=='*':
            print(number_1*number_2)
        elif operation=='/':
            print(number_1/number_2)
        elif operation=='%':
            print(number_1%number_2)
        elif operation=='**':
            print(number_1**number_2)
        else:
            print("invalid input")
    except exeception as e:
                print(e)
#---------------

try:
    a=123
    if a==123:
        print(b)
        raise NameError("name error")
    if a>0:
        raise ValueError("value error")
except NameError as ne:
    print(ne)
except NameError as ve:
    print(ve)
    
#-------------

try:
    age=int(input('enter your age:'))
except:
    print ('you have enter a n invalid value')
