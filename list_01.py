
# # create a list and display the number wich is not divisible by 10 and 5 
# list=[5,10,12,19,46,55,60,70,80,92,95]
# for i in list:
#     if(i%5==0 and i%10==0):
#         print(i)

# create a list with differenet types of value and display each value and its type
# list2=[20,"minarva",True,55.5]
# for i in list2:
    # if type(i)==int:
    #     print(i,'is','integer type')
    # elif type(i)==str:
    #    print(i,'is','string type') 
    # elif type(i)==bool:
    #     print(i,'is','bool type') 
    # else:
    #     print(i,'is','float type') 


 # create a list and check your list cantain how many int , how many string and how many float values are present 


# list=[20,50,66,'minarva','python','hello',True,False,45.9,88.3]
# count=0
# for i in list: 
#      if type(i)==int:
#       count=count+1
# print("list contains",count,"int") 
#      elif type(i)==str:
#       count=count+1
# print("list contains",count,"string")  
#     elif type(i)==bool:
#       count=count+1
# print("list contains",count,"bool") 
#    else:
#        print("list contain")         
            

# # create a list and replace int data with * 

# list=[20,50,66,'minarva','python','hello',True,False,45.9,88.3]
# for i in range(len(list)):
#      if type(list[i])==int:
#         list[i]="*"
# print(list)

# create a list and display element by index postive and negative both 

# list=[20,50,66,'minarva','python','hello',True,False,45.9,88.3]
# for i in range(len(list)):
#   print(list[i],"is in index",i,"and",-len(list)-i)
  

# list1=[10,20,30,42]
# list2=[1000,2000]
# print(list1>list2)
# print(list1==list2)
# print(list1<list2)
# print(list1<=list2)
# print(list1>=list2)
   
# list1=["baa","aaa"]
# list2=["bb","bbb"]
# print(list1>list2)
# print(list1==list2)
# print(list1<list2)
# print(list1<=list2)
# print(list1>=list2)
   

# 24/02/2022

# l=eval(input("enter first list:"))
# temp=l[0]
# l[0]=l[-1]
# l[-1]=temp
# print(l)
   
# l=eval(input("enter list:"))
# ele1=int(input("enter first element for swaping"))
# ele2=int(input("enter sec element for swaping"))
# pos1=l.index(ele1)
# pos2=l.index(ele2)
# temp=l[pos1]
# l[pos1]=l[pos2]
# l[pos2]=temp
# print(l)

# l=eval(input("enter list:"))
# a=min(l)
# b=max(l)
# print("min value is",a,"max value is",b)

# l=eval(input("enter list:"))
# sum=0
# for i in range(0,len(l)):
#   sum=sum+l[i]
# print(sum)

# l=eval(input("enter list:"))
# # l=[10,20,22.4,55]
# a=[]
# b=[]
# c=[]
# d=[]
# for i in range(len(l)):
#   if type(l[i])==int:
#     a.append(l[i])
#   elif type(i)==float:
#      b.append(l[i])
#   elif type(i)==bool:
#      c.append(l[i])
#   elif type(i)==complex:
#     d.append(l[i])
# print("list with integer",a)
# print("list with float",b)
# print("list with bool",c)
# print("list with complex",d)

# list=[10,15,20,25,30,35,40,50,55,60]
# missing=[]
# for i in range(list[0],list[-1]+1,5):
#   if i != list:
#     missing.append(i)
# print(missing)

# list=[10,15,20,25,30,35,40,50,55,60]
# missing=[]
# for i in range(list[0],list[-1]+1,5):
#   if i not in list:
#     missing.append(i)
# print(missing)


# list=[10,12,19,77,488,688,999,423,237]
# for i in list:
#   for j in list:
#     l=(i+1)-i
# print(i)  


