# Ecercise 1
class Book:
    book_count = 0  # class attribute (counter)

    def __init__(self, title):
        self.title = title
        Book.book_count += 1

b1 = Book("Python Basics")
b2 = Book("OOP Concepts")

print("Total books created:", Book.book_count)
print("------------------------\n")

# Exercise 2 - Student Class
class Student:
    school_name = "Vanier College"
    student_count = 0

    def __init__(self, name, program, grade):
        self.name = name
        self.program = program
        self.grade = grade
        Student.student_count += 1

    def display_info(self):
        print(f"{self.name} studies {self.program} at {Student.school_name}. Grade: {self.grade}")

student1 = Student("Ali Zafar: ", "Web Development 2", 76)
student2 = Student("Shah Hussain: ", "Content Management", 88)
student3 = Student("Zafar Kamran: ", "Python Programming", 92)

student1.display_info()
student2.display_info()
student3.display_info()

print("Total students:", Student.student_count)
print("------------------------\n")

# Exercise 3 - Product Class
class Product:
    category = "Electronics"
    tax_rate = 0.15

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_including_tax(self):
        return self.price + (self.price * Product.tax_rate)
    
product1 = Product("Keyboard", 100)
product2 = Product("Mouse", 50)
product3 = Product("Headphones", 140)

print("Prices with 15% tax:")
print(product1.price_including_tax())
print(product2.price_including_tax())
print(product3.price_including_tax())

# Changing tax rate to 20%
Product.tax_rate = 0.20

print("\nPrices with 20% tax:")
print(product1.price_including_tax())
print(product2.price_including_tax())
print(product3.price_including_tax())

print("------------------------\n")

# Exercise 4 - Employee Class
class Employee:
    company_name = "MontrealTech"
    bonus_rate = 0.10
    employee_count = 0

    def __init__(self, full_name, base_salary):
        self.full_name = full_name
        self.base_salary = base_salary
        Employee.employee_count += 1

    def calculate_bonus(self):
        return self.base_salary * self.bonus_rate

    def display_employee(self):
        print(f"{self.full_name} works at {Employee.company_name}. Salary: {self.base_salary}. Bonus: {self.calculate_bonus()}")

emp_a = Employee("Ali Zafar", 68000)
emp_b = Employee("Zanab Hussain", 80000)
emp_c = Employee("Zafar Kamran", 87000)

print("\n**** Initial Employees ****")
emp_a.display_employee()
emp_b.display_employee()
emp_c.display_employee()

# Change class bonus rate to 20%
Employee.bonus_rate = 0.20

print("\nAfter changing class bonus_rate to 0.20)")
emp_a.display_employee()
emp_b.display_employee()
emp_c.display_employee()

# Give one employee a custom bonus rate (50%)
emp_a.bonus_rate = 0.50

print("\nAfter giving emp_a custom bonus_rate (0.50)")
emp_a.display_employee()
emp_b.display_employee()
emp_c.display_employee()

# Change class bonus rate again to 5%
Employee.bonus_rate = 0.05

print("\nAfter changing class bonus_rate to 0.05)")
emp_a.display_employee()
emp_b.display_employee()
emp_c.display_employee()