from asyncio import selector_events
from tkinter import W


student={'id':[1001,1002,1003,1004],'name':['minarva','santosh','ayush','ritik'],'branch':['cse','ce','me','cse'],'no':[94384218,18463903,9846372,98746362],'issued':[]}
books={'name':['java','python','c++','c','DAA','DSA',''],'edition':[1.0,5.9,8,0,5],'author':['abc','xyz','pqr','mno']}
print("welcome to Library")
output='''
        select any option
        1.student login
        2.admin login
'''
print(output)
select=int(input("-"))

def registration():
    # student={'user1':{'id':1001,'name':'minarva','branch':'cse','phno':9438754715},'user2':{'id':1002,'name':'santosh','branch':'cse','phno':9438784715},'user3':{'id':1003,'name':'shreema','branch':'ce','phno':8738754715}}

    # books={'cg':{'B_id':'1s259','edition':'5th','author':'xyz','amount':4},'aca':{'B_id':'1s345','edition':'3rd','author':'pqs','amount':5}}
    user=int(input("enter the user id:"))
    user_name=input("enter name of the student:")
    user_branch=input("enter branch name:")
    user_phnno=input("enter phone no:")
    student['id'].append(user)
    student['name'].append(user_name)
    student['branch'].append(user_branch)
    student['no'].append(user_phnno)
    # print(student)
    print("your name has been registered")
    issue_book()
if select==1:
    username=str(input("enter user name:"))
    if username not in student['name']:
        print("u have not register yet, to register enter the following details-")
        registration()
    else:
        output2=   '''
                a.show books
                b.issue books
                c.return books
                d.issued books
                e.exit
            '''
        print(output2)
        def show_book():
                for i in books['name']:
                    print(i)
               
        def issue_book():    
                issue=input("enter book name to issue:")
                if issue in books['name']:
                    print(issue,"is issued by",username)
                    student['issued'].append(issue)
                    books['name'].remove(issue)
                else:
                 print("book is not available")
        
        def issued_books():
            for i in student['issued']:
                print(i)
            
 

        def return_book():
                returnn=input("enter book name to return:")
                if returnn in student['issued']:
                    print(returnn,"is return by",username)
                    student['issued'].remove(returnn)
                    books['name'].append(returnn)
        
        while True:
            select2=input("choose an option:")
            if select2=='a':
                show_book()
            elif select2=='b':
                 issue_book()
            elif select2=='c':
                 return_book() 
            elif select2=='d':
                 issued_books() 
            elif select2=='e':
                print("Thank you") 
                break
                   


                        
                        
        
        


