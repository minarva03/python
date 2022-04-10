# def fibo(n):
#     result=0
#     if n<=1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# print(fibo(4))

# x=list(filter(lambda x:type(x)==str or type(x)==bool,['a','b',11,22,True,False,55]))
# print(x)

# print(list(filter(lambda x:type(x)==str or type(x)==bool,['a','b',11,22,True,False,55])))

user=eval(input("enter the list items"))
x=list(filter(lambda x:type(x)==str or type(x)==bool,user))
print(x)