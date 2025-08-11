students = {}

#ref:
#details= {}
#details["student"] = {"name" : "sid", "age" : 30}
#print(details)

#student_id : full details(name,batch,attendance(total_days,present_days), terms(term1(subject:marks),(term2(subject:marks)))), 
#keys       : values   

def register_student(student_id,name,batch):
    students[student_id] = {"name":name, "batch":batch}
    print(students)
    

register_student("S1001","Siddarth","2024")