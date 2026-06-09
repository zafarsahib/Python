# This file defines the ShowStatus enum (group constants) 
# which represents the different statuses a movie show can have.

from enum import Enum

class ShowStatus(Enum):
    OPEN = "OPEN"
    SOLD_OUT = "SOLD_OUT"
    CANCELLED = "CANCELLED"
