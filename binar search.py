l=[4,6,7,9,5,1,2,7,3,8]
l.sort()
user=input("enter the number u want to search:")
for i in l:
    if user==l[i]:
        print(user,"found at", i, "location")
    else:
        print("number not found")