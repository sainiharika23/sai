class Employee:
    def getemployeeinfo(self):
        self.id=input('enter the ID:')
        self.name=input('enter the name:')
    def displayEmployeeinfo(self):
        print('ID=',self,id,'\n name=',self,name)


class perks(Employee):
    def getDetails(self):
        self.sal=int(input('enter salary:'))
    def displayinfo(self):
        print('salary=',self.sal)
p=perks()
p.getDetails()
p.displayinfo()
