
d1={}
d2={}
n=int(input("enter the number of first name:"))
m=int(input("enter the number of last name:"))
for i in range(n):
    Fname=input("enter the first name:")
    d1[i]=Fname
    i=i+1
for j in range(m):
    Lname=input("enter the last name:") 
    d2[j]=Lname
    j=j+1
print("Fname \t Lname")
for i in range(n):
    print(d1[i], "\t", d2[i])
print("afer shuffle")
print("Fname \t Lname")
for j in range(m):
    print(d1[j], "\t", d2[m-(j+1