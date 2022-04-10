num=int(input('enter number to check palindrome'))
temp=num
rev=0
while (num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if (temp==num):
    print('the number is palindrome')
else:
    print("the number is not palindrome")
