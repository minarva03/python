#remove empty list from list

# l1=[10,20,[],[],'minarva',40,50]
# l2=[]
# for i in l1:
#     if i!=[]:
#         if type(i)!=str:
#           l2.append(i)
# print(l2)   


#remove duplicates element from the list

# l1=[1,1,2,3,4,5,6,3,5]
# l2=[]
# for i in l1:
#    if i not in l2:
#       l2.append(i)
# print(l2)    


#find distance between two points

# x1=5
# y1=4
# x2=3
# y2=2
# D=((x2-x1)**2+(y2-y1)**2)/2
# print('the distance between two points are',D)

#TUPLES

#Product of tuple items

# t=(4,3,2,-1,19)
# mul=1
# for i in t:
#     mul=mul*i
# print(mul)

#sum of elements(pending)

# t1=(1,2,3,4,5)
# t2=(2,3,4,5,5)
# t3=()
# for i in t1:
#     for j in t2:
#        k=i+j
#         t3=
# print(t3)

#removing empty tuple from the list

# t1=((),(),('',),('a','b'),('a','b','c'),('d'))
# l1=list(t1)
# t2=()
# l2=list(t2)
# for i in l1:
#     if i!=():
#         if i not in l2:
#           l2.append(i)
# t2=tuple(l2)
# print(t2)      



#SET

#minimum value in a set

#element in a given set that are not in another set

# s=set()
# print(type(s))

# s={10,20,30}
# # s.add(66)
# l=[10,200,30,40,50]
# s.update(l,range(7))
# print(s)

# s={10,20,30}
# s1=s.copy()
# print(s1)

# s={23,44,10,20,30}
# print(s.pop())

# s={23,44,10,20,30}
# print(s.remove(80))

# s={23,44,10,20,30}
# s.discard(23)
# print(s)

# s={23,44,10,20,30}
# s.clear()
# print(s)