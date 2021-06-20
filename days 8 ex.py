#merge the two dictionaries
a={1,3,5,7,9}
b={2,4,6,8,10}
b.update(a)
print(b)

#descending to ascending
list1=[1,2,3,5,6,4,8]
lissort=sorted(list1)
deslist=sorted(list1,reverse=True)

print(deslist)
#list of dictionary iteam to sort without the help of function
list2={31,33,32,34,35,36,38,37,39,40}
sort=sorted(list2)
print(sort)
#list of dictionary iteamto sort within help of function
list3={2,4,5,7,8,1,9}

def function1(list3):
 list4=dict()
for key in sorted(list3):
    list4=sorted(list3)
    
    
    print(list3)
#first occurrenceof the word
def function3():
 user=input("enter the string:")
 word=("string is given by user:")
 return word.replace('string',user)

function3()

#first char change to capital letter

user=input("enter the string")

list5=user.capatalize()
print(list5)

#repeate item in the list
from collections import counter
list1=[1,1,2,3,4,5,4]
d=counter(list1)
print(d)
new_list=list([item for item in d if d[item]>1])
print(new_list)


def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

#

a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))
sum1=a+b+c
print(sum1)
user=int(input("Enter the number to divide sum!"))
if sum1% user==0:
    print("The given input divide")
else :
    print("The given input does not divide sum1")


#

from collections import Counter
def MMM(n_num):
    n = len(n_num)
    get_sum = sum(n_num)
    mean = get_sum / n
    print("Mean / Average is: " + str(mean))
    n_num.sort()
    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = n_num[n//2]
    print("Median is: " + str(median))
    data = Counter(n_num)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(mode) == n:
        get_mode = "No mode found"
    else:
        get_mode = "Mode is / are: " + ', '.join(map(str, mode))
    print(get_mode)



 #
a="Hello"
b="World"
tep=a
a=b
b=tep
print(a,b)


x = a
y = b
x, y = y, x
print(x,y)



#

def decToOctal(n):
    octalNum = [0] * 100
    i = 0
    while (n != 0):
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(octalNum[j], end="")
n=65
decToOctal(n)
        

