from user_types import (
    Customer,
    Staff,
    VIPCustomer
)

from movie_show import MovieShow
from movie_status import ShowStatus

from booking_exceptions import (
    InvalidTicketBookingError,
    MovieSoldOutError,
    MovieCancelledError,
    InvalidStatusError
)

print("========================================")
print("MOVIE TICKET BOOKING SYSTEM DEMONSTRATION")
print("========================================")

customer1 = Customer(
    "Ali Zafar",
    "ali_Zafar@email.com",
    "C101"
)

staff1 = Staff(
    "Batool Raza",
    "batoolrazah@email.com",
    "S201"
)

vip_customer = VIPCustomer(
    "Imam Raza",
    "imamrazah@email.com",
    "VIP001"
)

all_users = [customer1, staff1, vip_customer]

for user in all_users:
    user.display_info()
    print("--------------------------")

print("\nVALID MOVIE SHOW CREATION")

try:
    movie_show = MovieShow(
        "Interstellar",
        10
    )

    movie_show.display_info()

except ValueError as error:
    print("Movie Show Creation Failed:")
    print(error)

print("\nVALID BOOKING TEST")

try:
    movie_show.book_tickets(customer1, 3)
    movie_show.display_info()

except (
    InvalidTicketBookingError,
    MovieSoldOutError,
    MovieCancelledError
) as error:
    print("Booking Failed:")
    print(error)

print("\nINVALID BOOKING TEST")

try:
    movie_show.book_tickets(customer1, 10)

except InvalidTicketBookingError as error:
    print("Booking Failed:")
    print(error)

print("\nSOLD OUT MOVIE SHOW TEST")

try:
    movie_show.book_tickets(customer1, 5)
    movie_show.book_tickets(customer1, 2)

except (
    InvalidTicketBookingError,
    MovieSoldOutError
) as error:
    print("Booking Failed:")
    print(error)

movie_show.display_info()

try:
    movie_show.book_tickets(customer1, 1)

except MovieSoldOutError as error:
    print("Booking Failed:")
    print(error)

print("\nCANCELLED MOVIE SHOW TEST")

try:
    cancelled_show = MovieShow(
        "The Martian",
        50
    )

    cancelled_show.cancel_show()

    cancelled_show.book_tickets(customer1, 2)

except MovieCancelledError as error:
    print("Booking Failed:")
    print(error)

print("\nINVALID TOTAL SEATS TEST")

try:
    invalid_show = MovieShow(
        "Invalid Movie",
        0
    )

except ValueError as error:
    print("Movie Show Creation Failed:")
    print(error)

print("\nINVALID STATUS TEST")

try:
    movie_show.status = "OPEN"

except InvalidStatusError as error:
    print("Status Update Failed:")
    print(error)

print("\nREOPEN MOVIE SHOW TEST")

try:
    sold_out_show = MovieShow(
        "The Theory of Everything",
        5
    )

    sold_out_show.book_tickets(customer1, 5)

    sold_out_show.reopen_show()

    sold_out_show.display_info()

except Exception as error:
    print(error)

print("\nEND OF DEMONSTRATION")

