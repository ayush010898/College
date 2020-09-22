show dbs
use CollegeDetails
show collections
db.Student.insert([
    {name: "Ayush", USN: "1BM17CS018", branch: "CSE", year: "4", sec: "A",Hostel: "NO",home: "bangalore"},
    {name: "chandni", USN: "1BM17ECE020", branch: "ECE", year: "2", sec: "A",Hostel: "YES",home:"delhi"},
    {name: "Zeeshan", USN: "1BM17CSE080", branch: "CSE", year: "3", sec: "B",Hostel: "NO",home:"Bangalore"}
])
db.Teacher.insert([
    {name: "Tanay", emp_no: "CSE001", Dept: "CSE", emplomentYears: "4", designation:"associate", PHD: "no"},
    {name: "mohan", emp_no: "CSE003", Dept: "CSE", emplomentYears: "8", designation:"associate", PHD: "no"},
    {name: "Ekta", emp_no: "CSE009", Dept: "CSE", emplomentYears: "12",designation:"Dr", PHD: "yes"}
])
db.COE.insert([
    {name: "Ruchi", emp_no: "COE001", Dept: "COE", employmentYears: "4", Post: "Supervisor",city: "bangalore"},
    {name: "sarah", emp_no: "COE004", Dept: "COE", employmentYears: "1", Post: "Staff",city: "bangalore"},
    {name: "Raghav", emp_no: "COE007", Dept: "COE", employmentYears: "7", Post: "Evaluator",city: "agra"}
])
db.Library.insert([
    {name: "Ani", emp_no: "LIB018", Dept: "LIB", employmentYears: "8", Block: "New Building",city:"bangalore"},
    {name: "bhushan", emp_no: "LIB011", Dept: "LIB", employmentYears: "4", Block: "Old Building",city:"bangalore"},
    {name: "Anarghaya", emp_no: "LIB020", Dept: "LIB", employmentYears: "8", Block: "New Building",city:"mumbai"}
])
db.Admission.insert([
    {name: "Amog", emp_no: "ADM118", Dept: "ADM", employmentYears: "5", Location: "Admission Block",city: "bangalore"},
    {name: "bhavisha", emp_no: "ADM218", Dept: "ADM", employmentYears: "7", Location: "Admission Block",city: "delhi"},
    {name: "deepak", emp_no: "ADM018", Dept: "ADM", employmentYears: "7", Location: "Admission Block",city: "bangalore"}
])
db.collegeFestival.insert([
    {name: "Utsav", date: "10 April", Budget: "500000", Theme: "Cultural fest", Invites: "students",totalevents: "50"},
    {name: "IEEE Day", date: "10 OCT", Budget: "5000", Theme: "Social event", Invites: "students",totalevents: "10"},
    {name: "PhaseShift", date: "10 AUG", Budget: "50000", Theme: "Technical fest", Invites: "students",totalevents: "50"}
])
db.Admission.find()
db.COE.find()
db.Library.find()
db.Student.find()
db.Teacher.find()
db.collegeFestival.find().pretty()