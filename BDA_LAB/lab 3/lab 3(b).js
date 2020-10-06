show dbs
use Student
db.createCollection("details")
db.details.insert({_id: 1,name: "Ayush", RollNo: 10, Age: 22, ContactNo: 8547125698, EmailId: "a@g.com"})
db.details.insert({_id: 2,name: "ABC", RollNo: 11, Age: 25, ContactNo: 7981295698, EmailId: "b@h.com"})
db.details.insert({_id: 3,name: "XYZ", RollNo: 15, Age: 28, ContactNo: 9955784126, EmailId: "c@d.com"})
db.details.find().pretty()
db.details.update({RollNo: 10},{$set:{EmailId : "ayush@gmail.com"}})
db.details.find().pretty()
db.details.replaceOne({RollNo: 11}, {_id: 2,name: "FEM",Age: 25, ContactNo: 7981295698,EmailId:"b@h.com"})
db.details.find().pretty()
db.createCollection("HostelDeatails")
db.HostelDetails.drop()
show collections




