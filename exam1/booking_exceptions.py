# These are custom exceptions for the booking system.


class InvalidTicketBookingError(Exception):
    pass


class MovieSoldOutError(Exception):
    pass


class MovieCancelledError(Exception):
    pass


class InvalidStatusError(Exception):
    pass
