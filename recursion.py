# def fact(a):
#     result=0
#     if a==0:
#         result=1    
#     else:
#         result=a*fact(a-1)
#         return result
# print(fact(4))

# def fun(a):
#     print(a)
#     if a<10:
#         return fun(a+1)
# print(fun(1))

# l=['a',12,44,'d','e',69,10]
# def fun(i):
#     if i==-1:
#         return
#     elif type(l[i])==str:
#         l.pop(i)
#         print(l)
#         return fun(i-1)
#     else:
#         return fun(i-1)
# fun(6)



d={1:'a',2:'b',3:'c',4:'d'}
def fun(i):
        if i==4:
            return
        else:
            d1=d.values()
            d2=d.keys()
            print(d1)
            return fun(i+1)
fun(1)

