from enum import Enum


class TabState(Enum):
    COATING = "type_coating"
    DETERGENT = "type_detergent"
    INSECT = "?"


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


class FieldTankPos(Enum):
    F_TYPE = "type"
    F_LOCATION_NUM = "location nr"
    # F_SECTION = "section"
    # F_POSITION = "position"
    F_XMM = "x mm"
    F_YMM = "y mm"
    F_ZMM = "z mm"
    F_UX = "u.i"
    F_UY = "u.j"
    F_UZ = "u.k"
    F_VX = "v.i"
    F_VY = "v.j"
    F_VZ = "v.k"
    F_NX = "n.i"
    F_NY = "n.j"
    F_NZ = "n.k"


class FieldCali(Enum):
    F_SENSOR_TYPE = "sensor type"
    F_SENSOR_REF = "sensor ref"
    F_SENSOR_SERIAL_NUMBER = "sensor number"

    F_VERSUS_NAME = "versus"
    F_VERSUS_UNITE = "versus unite"

    F_PARAM_NAME = "param"
    F_PARAM_UNITE = "param unite"

    F_VERSUS_VALUE = "versus valeur"
    F_VALUE_READ = "valeur lue"
    F_VALUE_TRUTH = "valeur vraie"


class FieldSH(Enum):
    F_YEAR = "year"
    F_MONTH = "month"
    F_DAY = "day"
    F_HOUR = "hour"
    F_MINUTE = "minute"
    F_TIME_ZONE = "timezone"
    F_TYPE = "type"
    F_REF = "ref"
    F_SERIAL_NUMBER = "serial_number"
    F_ORDER = "order"
    F_LOCATION = "location"
    F_VALIDATION = "validation"


class FieldTkConfig(Enum):
    TK_LOCATION = "Tank location nr"
    REFERENCE_SENSOR_COATING = "Reference sensor/coating"
    SERIAL_NUMBER = "Serial number"
    ORDER = "Order"
    POSITION = "Position"


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


class TestMeanAttribute(Enum):
    ATTR = 'Attribute'
    VAL = 'Value'
    UNITY = 'Unity'


class ParamTable(Enum):
    PARAM = 'Param'
    UNITY = 'Unity_name'
    X = 'x'
    Y = 'y'
    Z = 'z'


class TestPointState(Enum):
    VALIDATED = 'Validated'
    CREATED = 'Created'
    NULL = 'None'


class TypeTestPointTable(Enum):
    PARAM_NAME = 'Param name'
    UNITY = 'Unity'


class TypeParamOfTypeTestPointHeader(Enum):
    TYPE_COATING = '<Type coating>'
    TYPE_DETERGENT = '<Type detergent>'
