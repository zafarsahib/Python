class CourseSection:
    def __init__(self, course_title, capacity):
        if not course_title or course_title.strip() == "":
            raise ValueError("Course title cannot be empty.")

        self.title = course_title
        self.capacity = capacity
        self.enrolled = 0  

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity_value):
        if capacity_value <= 0:
            raise ValueError("Capacity value must be greater than 0.")
        self.__capacity = capacity_value

    @property
    def enrolled(self):
        return self.__enrolled

    @enrolled.setter
    def enrolled(self, enrolled_value):
        if enrolled_value < 0:
            raise ValueError("Enrolled valuecannot be negative.")
        if hasattr(self, "_CourseSection__capacity") and enrolled_value > self.__capacity:
            raise ValueError("Enrolled cannot exceed capacity.")
        self.__enrolled = enrolled_value

    def register_student(self):
        if self.enrolled >= self.capacity:
            raise ValueError("Cannot enroll: course is full.")
        self.enrolled += 1

    def drop_student(self):
        if self.enrolled <= 0:
            raise ValueError("Cannot drop: no students enrolled.")
        self.enrolled -= 1

    def display_info(self):
        print(f"Course: {self.title}")
        print(f"Capacity: {self.capacity}")
        print(f"Enrolled: {self.enrolled}")
        print("-" * 30)
