#01_variable length argument in python

# def fun(*args):
#     for i in args:
#         print(i)
# fun(10,20,30,40)

#02_return multiple values

# def fun(a,b):
#     return a+b,a-b
# print(fun(40,10))

#03_default argument

# def fun(a,b=50):
#     return a*b
# print(fun(40))

#04_recursive function

# def fun(num):
#     if num:
#      return num + fun(num-5)
#     else:
#         return 0
# print(fun(40))

#05_different function same argument

# def fun1(name,age):
#     print(name,age)
# fun1("minarva",21)
# fun2=fun1
# fun2("shreema",20)

#even num between 4 to 30 in a list

# L=[]
# for i in range(4,31):
#     if i%2==0:
#         L.append(i)
# print(L)

#largest item in a list

# L=[66,43,12,11,9,56,22]
# print(max(L))

#length of list
#01-naive method
# L=[1,2,3,4,5,6]
# print("the list is:"+ str(L))
# count=0
# for i in L:
#     count=count+1
# print("the lenght of the list is:" + str(count))

#02-len()method
# L=[1,2,3,4,5,6]
# print("length of the list is:",len(L))


