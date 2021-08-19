import sys
sys.path.insert(1, '/Users/anish/Documents/layered')
from servicelayer import addservice
from dao import dbcon

obj1=addservice.EmpDetails()
while(True):
    print("1.Add Employees")
    print("2.View all Employees")
    print("3.Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        Employeename=input("enter the Employees name - ")
        Age=input("enter the Age- ")
        obj1.addEmployeeDetails(Employeename,Age)
        result=dbcon.Collection_name.insert_many(addservice.datalist)
        print("Inserted")
    if choice==2:
        result = dbcon.Collection_name.find()
        l=[]
        print(result)
        for i in result:
            l.append(i)
            print(i)
        print(l)    
    if choice==3:

        break    
        
