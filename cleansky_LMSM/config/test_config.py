from enum import Enum


class DataType(Enum):
    CO = "Coating"
    F_D = "Flight data"
    P = "Pictures"
    S_D = "Sensor data"


class FlightDataState(Enum):
    PARAM = "Param name"
    VALIDATE = "Validate"
    TIME_BEGIN = "Time begin"
    TIME_END = "Time end"


class SensorDataState(Enum):
    LOCATION = "Location"
    REF_SENSOR = "Ref sensor"
    N_SENSOR = "Num sensor"
    PARAM = "Parameter"


class CoatingsState(Enum):
    COATING_TYPE = "Coating Type"
    COATING_NUMBER = "Coating Number"


class DataState(Enum):
    VALIDATED = "True"
    NOT_VALIDATE = "False"
