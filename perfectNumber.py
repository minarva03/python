num=int(input('enter the number:'))
sum=0
for i in range(1,num):
    if (num%i==0):
        sum=sum+i
if (sum==num):
    print('the number is perfect number')
else:
    print('the number is not a perfect number')