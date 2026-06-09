# movie_show.py

from booking_constants import MAX_TICKETS_PER_BOOKING
from movie_status import ShowStatus

from booking_exceptions import (
    InvalidTicketBookingError,
    MovieSoldOutError,
    MovieCancelledError,
    InvalidStatusError
)


class MovieShow:

    def __init__(self, movie_title, total_seats):

        if not movie_title.strip():
            raise ValueError("Movie title cannot be empty.")

        self.__movie_title = movie_title

        self.total_seats = total_seats

        self.__tickets_sold = 0
        self.__status = ShowStatus.OPEN

    @property
    def total_seats(self):
        return self.__total_seats

    @total_seats.setter
    def total_seats(self, value):

        if value <= 0:
            raise ValueError("Total number of seats must be greater than zero.")

        if hasattr(self, "_MovieShow__tickets_sold"):
            if self.__tickets_sold > value:
                raise ValueError(
                    "Total seats cannot be less than tickets already sold."
                )

        self.__total_seats = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):

        if not isinstance(value, ShowStatus):
            raise InvalidStatusError("Status must be a valid ShowStatus value.")

        self.__status = value

    @property
    def remaining_seats(self):
        return self.__total_seats - self.__tickets_sold

    # Bonus B
    @property
    def is_sold_out(self):
        return self.remaining_seats == 0

    def book_tickets(self, customer, ticket_quantity):

        if ticket_quantity <= 0:
            raise InvalidTicketBookingError("Number of tickets must be greater than zero.")

        if ticket_quantity > MAX_TICKETS_PER_BOOKING:
            raise InvalidTicketBookingError(
                f"Maximum {MAX_TICKETS_PER_BOOKING} tickets allowed per booking."
            )

        if self.__status == ShowStatus.CANCELLED:
            raise MovieCancelledError("Movie show has been cancelled.")

        if self.__status == ShowStatus.SOLD_OUT:
            raise MovieSoldOutError("Movie show is sold out.")

        if ticket_quantity > self.remaining_seats:
            raise InvalidTicketBookingError("Not enough available seats.")

        self.__tickets_sold += ticket_quantity

        print("\nBooking Successful!")
        print(f"Customer: {customer._full_name}")
        print(f"Tickets Booked: {ticket_quantity}")
        print(f"Remaining Seats: {self.remaining_seats}")

        if self.__tickets_sold == self.__total_seats:
            self.__status = ShowStatus.SOLD_OUT

    def cancel_show(self):

        self.__status = ShowStatus.CANCELLED

        print(f"\nMovie '{self.__movie_title}' has been cancelled.")

    def reopen_show(self):

        if self.__status == ShowStatus.CANCELLED:
            raise InvalidTicketBookingError(
                "Cancelled movie shows cannot be reopened."
            )

        if self.__status != ShowStatus.SOLD_OUT:
            raise InvalidTicketBookingError(
                "Only sold-out shows can be reopened."
            )

        if self.remaining_seats == 0:
            raise InvalidTicketBookingError(
                "Cannot reopen: no available seats."
            )

        self.__status = ShowStatus.OPEN

        print(f"\nMovie '{self.__movie_title}' has been reopened.")

    def display_info(self):

        print("\n===================================")
        print("Movie Show Details")
        print("===================================")

        print(f"Movie Title: {self.__movie_title}")
        print(f"Total Seats: {self.__total_seats}")
        print(f"Tickets Sold: {self.__tickets_sold}")
        print(f"Remaining Seats: {self.remaining_seats}")
        print(f"Booking Status: {self.__status.value}")

        print("===================================")