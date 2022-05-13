"""
The reason for using enum types is to ensure type safety.
This module covers various enumeration types for sensor life cycle.
"""
from enum import Enum


class State(Enum):
    """Because the database layer uses varchar as the field of the sensor_location table to store information, in
    order to simplify the complexity of the model layer, the value of the enumeration type is set to a string, which
    matches the table structure. The field value can be obtained directly by calling the value interface at the
    model layer."""
    ORDER = "order"
    OUT_OF_ORDER = "out of order"
    IN_REPAIRING = "repairing"
    REMOVED = "removed"


class Loc(Enum):
    IN_CONFIG = "in config"
    IN_STORE = "in store"


if __name__ == "__main__":
    print(State.ORDER == State.ORDER)
    ls = [item.value for item in State]
    print(ls)
