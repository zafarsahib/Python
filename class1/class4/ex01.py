class Employee:
    # class attributes
    bonus = 0.25
    company_name = "Montreal Tech"

    def __init__(self, name, sales_count):
        # instance attributes
        self.name = name
        self.sales_count = sales_count

    def calculate_salary(self):
        base_salary = 500

        if self.sales_count > 10:
            total_salary = base_salary + (base_salary * Employee.bonus)
        else:
            total_salary = base_salary

        return total_salary


# Example usage
emp1 = Employee("Alice", 5)
emp2 = Employee("Ali Zafar", 20)

print(emp1.name, "salary:", emp1.calculate_salary())
print(emp2.name, "salary:", emp2.calculate_salary())