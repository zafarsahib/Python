from student_record import StudentRecord
from course_section import CourseSection

print("****** VALID CASES ******")

# Valid student
student = StudentRecord("Ali Zafar", 3.2, 30)
student.display_info()

student.add_credits(3)
student.update_gpa(3.8)
student.display_info()

# Valid course
course = CourseSection("Python Programming", 2)
course.display_info()

course.register_student()
course.register_student()
course.display_info()

course.drop_student()
course.display_info()

print("\n****** INVALID CASES ******")

# Invalid GPA
try:
    student.update_gpa(5.0)
except ValueError as e:
    print("Error:", e)

# Negative credits
try:
    student.add_credits(-5)
except ValueError as e:
    print("Error:", e)

# Empty name
try:
    bad_student = StudentRecord("", 3.0, 10)
except ValueError as error:
    print("Error:", error)

# Invalid course title
try:
    bad_course = CourseSection("", 10)
except ValueError as error:
    print("Error:", error)

# Capacity = 0
try:
    bad_course = CourseSection("Math", 0)
except ValueError as error:
    print("Error:", error)

# Over-enrollment
try:
    course.register_student()
except ValueError as error:
    print("Error:", error)

# Drop below zero
try:
    course.drop_student()
    course.drop_student()
except ValueError as error:
    print("Error:", error)
