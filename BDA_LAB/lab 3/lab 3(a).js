use Database
db.createCollection("Customer")
db.customer.insert({cust_id:1,acc_bal:1500,acc_type:"z"})
db.customer.insert({cust_id:2,acc_bal:1800,acc_type:"a"})
db.customer.insert({cust_id:1,acc_bal:2500,acc_type:"z"})
db.customer.insert({cust_id:2,acc_bal:1500,acc_type:"a"})
db.customer.insert({cust_id:1,acc_bal:5500,acc_type:"z"})
db.customer.find().pretty()
db.customer.find({acc_bal:{$gt:1200}, acc_type:"z"})
db.createCollection("extra")
db.extra.drop()
db.customer.aggregate([
    {
        $group: {
            _id: "$cust_id",
            min_bal: {$min: "$acc_bal"},
            max_bal: {$max: "$acc_bal"}
        }
    }
])