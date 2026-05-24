class StudentRecord:
    def __init__(self, name, gpa, credits):
        if not name or name.strip() == "":
            raise ValueError("Name cannot be empty.")

        self.name = name
        self.gpa = gpa
        self.credits = credits

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, gpa_value):
        if not (0.0 <= gpa_value <= 4.0):
            raise ValueError("GPA must be between 0.0 and 4.0.")
        self.__gpa = gpa_value

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, credits_value):
        if credits_value < 0:
            raise ValueError("Your Credits can not be negative.")
        self.__credits = credits_value

    def add_credits(self, amount):
        if amount < 0:
            raise ValueError("You Can not add negative credits.")
        self.credits += amount

    def update_gpa(self, gpa_value):
        self.gpa = gpa_value  # uses setter validation

    def display_info(self):
        print(f"Student: {self.name}")
        print(f"GPA: {self.gpa}")
        print(f"Credits: {self.credits}")
        print(f"Status: {self.academic_status}")
        print("-" * 30)

    # Challenge 1: Computed property
    @property
    def academic_status(self):
        if self.gpa >= 3.5:
            return "For your Honours"
        elif self.gpa >= 2.0:
            return "Good gpa Standing"
        else:
            return "You are at Risk"
        