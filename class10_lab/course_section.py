class CourseSection:
    def __init__(self, title, capacity):
        if not title.strip():
            raise ValueError("Course title cannot be empty.")

        self.title = title
        self.capacity = capacity   # property
        self.enrolled = 0          # property
        self.__waitlist = 0        # private

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value > 0:
            self.__capacity = value
        else:
            raise ValueError("Capacity must be greater than 0.")

    @property
    def enrolled(self):
        return self.__enrolled

    @enrolled.setter
    def enrolled(self, value):
        if value < 0:
            raise ValueError("Enrolled cannot be negative.")
        if value > self.capacity:
            raise ValueError("Enrolled cannot exceed capacity.")
        self.__enrolled = value

    # Waitlist - read-only property
    @property
    def waitlist(self):
        return self.__waitlist

    def register_student(self):
        if self.enrolled < self.capacity:
            self.enrolled += 1
        else:
            self.__waitlist += 1

    def drop_student(self):
        if self.enrolled <= 0:
            raise ValueError("No students to drop.")

        self.enrolled -= 1

        if self.waitlist > 0:
            self.__waitlist -= 1
            self.enrolled += 1

    def add_to_waitlist(self):
        self.__waitlist += 1

    def remove_from_waitlist(self):
        if self.__waitlist <= 0:
            raise ValueError("Waitlist is empty.")
        self.__waitlist -= 1

    def display_info(self):
        print(f"Course: {self.title}")
        print(f"Capacity: {self.capacity}")
        print(f"Enrolled: {self.enrolled}")
        print(f"Waitlist: {self.waitlist}")
        print("-" * 30)
        
