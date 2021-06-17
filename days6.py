#merge two dictionaries
dict1={"dhoni","raina","sam","faf"}
dict2={"captain","vice captain","fast bolwer","opener batman"}
print(dict2.update(dict1))
print(dict2)

#remove a key fro the dictionary
dict2.pop()
print(dict2)

#map two list
dic1=['dhoni','sam','raina','faf']
dic2=['captain','fast bowler','vice captain','opener batsman']
res1={dic1[i]:dic2[i] for i in range(len(dic1))}
print(res1)


dic1=['dhoni','sam','raina','faf']
dic2=['captain','fast bowler','vice captain','opener batsman']
res2=dict(zip(dic1,dict2))
print(res2)


#find the length of a set
dic1=['dhoni','sam','raina','faf']
print(dic1,len(dic1))

#intersection of sets
d1={'dhoni','sam','raina','faf'}
d2={'dhoni','faf','jaddu','sam','sai'}
print(d1.intersection(d2))
