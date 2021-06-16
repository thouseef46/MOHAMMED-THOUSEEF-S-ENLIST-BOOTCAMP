x=input("enter the name")
print("enter the name"+x)

list=[10,20,30,40,'xyz',50,60]
list.append([70])
print(list)
list.extend([99,100])
print(list)
list.insert(8,96)
print(list)
del list[10]
list.pop()
print(list)
list.remove(40)
print(list)

#max and min
a=[10,20,30,40,50,60,90,120]
max=max(a)
print('maximum element in list',max)
min=min(a)
print('mininum element in list',min)


#tuple
tuple=('red','bule','black')
s=sorted(tuple)
print("tuple before sorted",tuple)
print("reverse the tuple",sorted(tuple,reverse=True))
print("sorted tuple",s)

#----
value=(10,20,30,40,50)
my_tuple= list(value)
print(my_tuple)

