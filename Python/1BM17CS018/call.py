class calldetail:
    def __init__(self,a,b,c,d):
        self.calledby = a
        self.calledto = b
        self.duration = c
        self.typecall = d

    def displayDetails(self):
        print("caller phone no. :",self.calledby)
        print("reciever phone no. :",self.calledto)
        print("duration :",self.duration)
        print("call type :",self.typecall)

class util:
    def __init__(self):
        self.list_call_objects=None
    def parseCustomer(self,callList):
        call_detail= []
        for i in range(len(callList)):
            res=callList[i].split(',')
            call_detail.append(calldetail(res[0],res[1],res[2],res[3]))
            call_detail[i].displayDetails()
            print()

call='996264589,9595954136,23,STD'
call2='1646565165,687641361,45,local'
call3='4968446864,486454599,8,ISD'

callList=[call,call2,call3]
util().parseCustomer(callList)