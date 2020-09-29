use Company
db.createCollection("Employee")
db.createCollection("Department")
show collections

//insert queries of 3 types (insert, update, save)
db.Employee.insert({_id: 1,name: "Ayush", age: 25, salary: 120000, position: "CEO"})
db.Employee.update({_id: 2,name: "Sarvesh", age: 26, salary: 580000},{$set:{position: "CFO"}},{upsert:true})
db.Employee.save({_id: 3,name: "Rahul", age: 30, salary: 500000, position: "Junior Associate"})
db.Employee.find()

//insert queries of 3 types (insert, update, save)
db.Department.insert({_id:1,Name:"IT",NoOfEmp:200,HOD:"Aditya"})
db.Department.update({_id:2,Name:"HR",NoOfEmp:100},{$set:{HOD:"Jatin"}},{upsert:true})
db.Department.save({_id:3,Name:"Customer Division",NoOfEmp:300,HOD:"Akash"})
db.Department.find()

//inserting a new filed using update
db.Employee.update({_id: 1},{$set:{department: 1002}})
db.Employee.update({_id: 2},{$set:{department: 1003}})
db.Employee.update({_id: 3},{$set:{department: 1008}})
db.Employee.find()

//remove a field age from id 2
db.Employee.update({_id: 2},{$unset:{age: 26}})

//name of employee starting from A
db.Employee.find({name:/^A/}).pretty()

//employees with emp number between 1001 and 1005
db.Employee.find({department: {$gt : 1000, $lt : 1006}}).pretty()

//employees with age greater than 30
db.Employee.find({age : {$gt : 30}}).pretty()







