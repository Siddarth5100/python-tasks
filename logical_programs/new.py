# Dictionary to store student records
students = {}

# 1. Register a new student
def register_student(student_id, name, batch):
    if student_id in students:
        print(f"Student with ID {student_id} already exists.")
        return
    students[student_id] = {
        "name": name,
        "batch": batch,
        "attendance": {"total_days": 0, "present_days": 0},
        "terms": {}
    }

# 2. Add term result (marks for subjects)
def add_term_result(student_id, term_name, subject_marks_dict):
    if student_id in students:
        students[student_id]["terms"][term_name] = subject_marks_dict
    else:
        print(f"Student {student_id} not found.")

# 3. Update a subject mark in a specific term
def update_subject_mark(student_id, term, subject, new_mark):
    try:
        students[student_id]["terms"][term][subject] = new_mark
    except KeyError:
        print("Invalid student ID / term / subject.")

# 4. Record attendance
def record_attendance(student_id, present_days, total_days):
    if student_id in students:
        students[student_id]["attendance"]["present_days"] = present_days
        students[student_id]["attendance"]["total_days"] = total_days
    else:
        print("Student not found.")

# 5. Calculate average marks of a student across all terms
def calculate_average(student_id):
    if student_id not in students:
        return 0
    total = count = 0
    for term in students[student_id]["terms"].values():
        for mark in term.values():
            total += mark
            count += 1
    return round(total / count, 2) if count != 0 else 0

# 6. Calculate attendance percentage
def calculate_attendance_percentage(student_id):
    att = students[student_id]["attendance"]
    if att["total_days"] == 0:
        return 0
    return round((att["present_days"] / att["total_days"]) * 100, 2)

# 7. Get topper of a specific term
def get_topper_by_term(term):
    top_student = None
    top_avg = -1
    for student_id, info in students.items():
        if term in info["terms"]:
            marks = info["terms"][term].values()
            avg = sum(marks) / len(marks)
            if avg > top_avg:
                top_avg = avg
                top_student = (info["name"], student_id, round(avg, 2))
    return top_student

# 8. Rank students by overall average (within a batch)
def rank_students_by_overall_average(batch):
    ranking = []
    for student_id, info in students.items():
        if info["batch"] == batch:
            avg = calculate_average(student_id)
            ranking.append((student_id, info["name"], avg))
    ranking.sort(key=lambda x: x[2], reverse=True)
    return ranking

# 9. Generate a full report for a student
def generate_student_report(student_id):
    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]
    print(f"\n🎓 Student Report: {student['name']} ({student_id})")
    print(f"Batch: {student['batch']}")
    
    attendance_pct = calculate_attendance_percentage(student_id)
    print(f"Attendance: {attendance_pct}%")

    term_avgs = []
    for term, marks in student["terms"].items():
        avg = round(sum(marks.values()) / len(marks), 2)
        term_avgs.append(avg)
        print(f"{term} Average: {avg}")

    if term_avgs:
        overall = round(sum(term_avgs) / len(term_avgs), 2)
        print(f"Overall Average: {overall}")

    # Show topper of Term 2 (example)
    topper = get_topper_by_term("Term 2")
    if topper:
        print(f"Top Performer: {topper[0]} in Term 2 with {topper[2]} average")
