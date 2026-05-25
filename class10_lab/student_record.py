class StudentRecord:
    def __init__(self, name, gpa, credits):
        if not name.strip():
            raise ValueError("Name cannot be empty.")

        self.name = name
        self.gpa = gpa        
        self.credits = credits 

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0:
            self.__gpa = value
        else:
            raise ValueError("GPA must be between 0.0 and 4.0.")

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, value):
        if value >= 0:
            self.__credits = value
        else:
            raise ValueError("Credits cannot be negative.")

    def add_credits(self, amount):
        if amount < 0:
            raise ValueError("Cannot add negative credits.")
        self.credits += amount

    def update_gpa(self, value):
        self.gpa = value

    def display_info(self):
        print(f"Student: {self.name}")
        print(f"GPA: {self.gpa}")
        print(f"Credits: {self.credits}")
        print(f"Status: {self.academic_status}")
        print("-" * 30)

    # Challenge 1 - read-only computed property
    @property
    def academic_status(self):
        if self.gpa >= 3.5:
            return "Honours"
        elif self.gpa >= 2.0:
            return "Good Standing"
        else:
            return "At Risk"
        