import time
datalist=[]
class EmpDetails:
    def addEmployeeDetails(self,Employeename,Age):
        current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
        dict1={"EmployeeName":Employeename,"Age":Age,"AddOn":current_time}
        datalist.append(dict1)