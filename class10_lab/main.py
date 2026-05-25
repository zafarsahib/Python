from student_record import StudentRecord
from course_section import CourseSection

def transfer_student(source, destination):
    if source.enrolled > 0 and destination.enrolled < destination.capacity:
        source.drop_student()
        destination.register_student()
    else:
        print("Error: Transfer not possible")

print("\n===== VALID CASES =====\n")

student = StudentRecord("Ali", 3.2, 30)
student.display_info()

student.add_credits(5)
student.update_gpa(3.8)
student.display_info()

course = CourseSection("Python Programming", 2)

course.register_student()
course.register_student()

course.display_info()


print("\n===== WAITLIST TESTS =====\n")

waitlist_course = CourseSection("Data Structures", 2)

waitlist_course.register_student()
waitlist_course.register_student()
waitlist_course.register_student()
waitlist_course.register_student()

waitlist_course.display_info()

waitlist_course.drop_student()
waitlist_course.display_info()

print("\n===== TRANSFER TESTS =====\n")

course_a = CourseSection("Algorithms", 2)
course_b = CourseSection("Databases", 2)

course_a.register_student()
course_a.register_student()
course_b.register_student()

print("Before transfer:")
course_a.display_info()
course_b.display_info()

transfer_student(course_a, course_b)

print("After transfer:")
course_a.display_info()
course_b.display_info()

print("\n===== INVALID CASES =====\n")

bad_gpa = 5.0
if 0.0 <= bad_gpa <= 4.0:
    student.update_gpa(bad_gpa)
else:
    print("Error: GPA must be between 0.0 and 4.0")

bad_credits = -10
if bad_credits >= 0:
    student.add_credits(bad_credits)
else:
    print("Error: Credits cannot be negative")

name = ""
if name.strip():
    bad_student = StudentRecord(name, 3.0, 10)
else:
    print("Error: Name cannot be empty")

title = ""
capacity = 0

if title.strip() and capacity > 0:
    bad_course = CourseSection(title, capacity)
else:
    print("Error: Invalid course setup")

empty_course = CourseSection("Physics", 2)
if empty_course.enrolled > 0:
    empty_course.drop_student()
else:
    print("Error: Cannot drop from empty course")

if empty_course.waitlist > 0:
    empty_course.remove_from_waitlist()
else:
    print("Error: Waitlist already empty")


print("\n===== END OF TESTS =====\n")

