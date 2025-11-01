def read_marks(filename):
    """Reads student marks from file and stores them in a dictionary"""
    students = {}

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip() 
                if not line:  
                    continue
                try:
                    student_id, name, subject, marks = line.split(",")
                    marks = int(marks)
                except ValueError:
                    print("Invalid line found, skipping:", line)
                    continue

                if student_id not in students:
                    students[student_id] = {
                        "name": name,
                        "subjects": {}
                    }
                students[student_id]["subjects"][subject] = marks

    except FileNotFoundError:
        print("File not found! Please check the filename.")
        return {}

    return students

def generate_report(students):
    """Creates a report for each student"""
    report_data = []
    for student_id, info in students.items():
        name = info["name"]
        subjects = info["subjects"]
        total = sum(subjects.values())
        average = total / len(subjects)
        highest_subject = max(subjects, key=subjects.get)
        lowest_subject = min(subjects, key=subjects.get)
        report_data.append({
            "id": student_id,
            "name": name,
            "total": total,
            "average": average,
            "highest": (highest_subject, subjects[highest_subject]),
            "lowest": (lowest_subject, subjects[lowest_subject])
        })

    report_data.sort(key=lambda x: x["average"], reverse=True)
    return report_data


def write_summary(filename, report_data):
    """Writes the final report to a text file"""
    with open(filename, "w") as file:
        for student in report_data:
            file.write(f"Student ID: {student['id']}\n")
            file.write(f"Name: {student['name']}\n")
            file.write(f"Total Marks: {student['total']}\n")
            file.write(f"Average Marks: {student['average']:.2f}\n")
            file.write(f"Highest Scored Subject: {student['highest'][0]} ({student['highest'][1]})\n")
            file.write(f"Lowest Scored Subject: {student['lowest'][0]} ({student['lowest'][1]})\n")
            file.write("-" * 40 + "\n")



students = read_marks("marks.txt")

if students:
    report = generate_report(students)
    write_summary("report.txt", report)
    print("Report generated successfully! Check 'report.txt'")
else:
    print("No data found to generate report.")
