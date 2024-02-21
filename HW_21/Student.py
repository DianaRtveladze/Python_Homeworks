import json
from Address import Address


class Student:
    row_id = 0 

    def __init__(self, name, mark, address):
        Student.row_id += 1
        self.row_id = Student.row_id
        self.name = name
        self.mark = mark
        self.address = address
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark >= 91:
            return 'A'
        elif 81 <= self.mark <= 90:
            return 'B'
        elif 71 <= self.mark <= 80:
            return 'C'
        else:
            return 'D'


address1 = Address("Tbilisi", "Saburtalo")
address2 = Address("Tbilisi", "Gldani-7-11-4-93")
address3 = Address("Tbilisi", "Leselidzs str. 25")
address4 = Address("Tbilisi", "Varketili IV 407-5-123")


student1 = Student("Paata", 87, address1)
student2 = Student("Demetre", 100, address2)
student3 = Student("Alexander", 100, address2)
student4 = Student("Teona", 92, address2)
student5 = Student("Nino", 99, address3)
student6 = Student("Andria", 87, address4)


def address_serializer(obj):
    if isinstance(obj, Address):
        return {"city": obj.city, "street": obj.street}
    raise TypeError("Type not serializable")
# Create instances of Address
address1 = Address("Tbilisi", "Saburtalo")
address2 = Address("Tbilisi", "Gldani-7-11-4-93")
address3 = Address("Tbilisi", "Leselidzs str. 25")
address4 = Address("Tbilisi", "Varketili IV 407-5-123")

# Create instances of Student
student1 = Student("Paata", 87, address1)
student2 = Student("Demetre", 100, address2)
student3 = Student("Alexander", 100, address2)
student4 = Student("Teona", 92, address2)
student5 = Student("Nino", 99, address3)
student6 = Student("Andria", 87, address4)

with open("students.json", "w") as file:
    students_data = [
        vars(student) for student in [student1, student2, student3, student4, student5, student6]
    ]
    json.dump(students_data, file, indent=2, default=address_serializer)

# Read the file
with open("students.json", "r") as file:
    students_data = json.load(file)

# Update attributes and add a new attribute
for student_data in students_data:
    student_data["mark"] = str(student_data["mark"])  # Convert mark to string
    student_data["grade"] = student_data["grade"] if "grade" in student_data else "Not Assigned"

# Save the updated data to another file
with open("updated_students.json", "w") as file:
    json.dump(students_data, file, indent=2)

print("Files saved successfully.")