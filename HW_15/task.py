import csv
import os

def add_student_to_csv(id, name, age, grade, subject_name, marks, filename='students.csv'):
    header = ['id', 'name', 'age', 'grade', 'subject_name', 'marks']
    student_data = [id, name, age, grade, subject_name, marks]

    if not os.path.isfile(filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student_data)

def read_all_students(filename='students.csv'):
    students = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

def read_specific_student(student_id, filename='students.csv'):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == student_id:
                return row
    return None

def update_student_score(student_id, subject_name, new_marks, filename='students.csv'):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row[0] == student_id and row[4] == subject_name:
            row[5] = new_marks

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)



add_student_to_csv(1, 'John Doe', 20, 'A', 'Math', 95)
add_student_to_csv(2, 'Jane Smith', 22, 'B', 'English', 85)

all_students = read_all_students()
print("All Students:")
print(all_students)

specific_student = read_specific_student('1')
print("\nSpecific Student:")
print(specific_student)

update_student_score('1', 'Math', 98)
updated_student = read_specific_student('1')
print("\nUpdated Student:")
print(updated_student)
