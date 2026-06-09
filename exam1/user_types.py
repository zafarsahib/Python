# This file defines the User, Customer, Staff, 
# and VIPCustomer classes for the booking system.


class User:

    def __init__(self, full_name, email_address):

        if not full_name.strip(): # strip() is used to remove whitespace
            raise ValueError("User name cannot be empty.")

        if not email_address.strip():
            raise ValueError("Email address cannot be empty.")

        self._full_name = full_name
        self._email_address = email_address

    def display_info(self):
        print(f"Name: {self._full_name}")
        print(f"Email: {self._email_address}")


class Customer(User):

    def __init__(self, full_name, email_address, customer_number):

        super().__init__(full_name, email_address)

        if not customer_number.strip():
            raise ValueError("Customer number cannot be empty.")

        self.__customer_number = customer_number

    def display_info(self):

        print("Customer Information")
        print(f"Name: {self._full_name}")
        print(f"Email: {self._email_address}")
        print(f"Customer Number: {self.__customer_number}")


class Staff(User):

    def __init__(self, full_name, email_address, staff_id):

        super().__init__(full_name, email_address)

        if not staff_id.strip():
            raise ValueError("Staff ID cannot be empty.")

        self.__staff_id = staff_id

    def display_info(self):

        print("Staff Information")
        print(f"Name: {self._full_name}")
        print(f"Email: {self._email_address}")
        print(f"Staff ID: {self.__staff_id}")


# Bonus C section: optional VIPCustomer class
class VIPCustomer(Customer):

    def __init__(self, full_name, email_address, customer_number):
        super().__init__(
            full_name,
            email_address,
            customer_number
        )

    def display_info(self):

        print("VIP Customer Information")
        super().display_info()
