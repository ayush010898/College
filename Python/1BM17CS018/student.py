class admission:
    def __init__(self):
        self.id=0
        self.age=0
        self.marks=0

    def validateMarks(self,marks):
        if marks >= 0 and marks <= 100:
            return True
        else :
            print("enter marks between 0 and 100")
            return False

    def validateAge(self,age):
        if age >= 20:
            return True
        else:
            print("age below 20")
            return False

    def checkQualification(self,age,marks):
        if self.validateMarks(marks) and self.validateAge(age):
            if marks >= 65:
                return True
            elif marks < 65:
                print("marks less than 65.")
                return False

    def setDetails(self,s_id,age,marks):
         self.id = s_id
         self.age = age
         self.marks = marks

    def getDetails(self):
         print("id: ",self.id)
         print("age: ",self.age)
         print("marks: ",self.marks)\

num = int(input("enter number of students"))
while num:
    print()
    a=admission()
    sid=int(input("Student id:"))
    age=int(input("Student age:"))
    marks=int(input("Student marks:"))
    if a.checkQualification(age,marks):
        a.setDetails(sid,age,marks)
        print("Qualified")
        a.getDetails()
    else:
        print("Not qualified")   
    print()         
    num = num - 1     