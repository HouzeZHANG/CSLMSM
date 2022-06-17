"""It must be ensured that the field names of the csv file are legal and match the field names in the software,
otherwise the software will not work properly"""
from enum import Enum


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


if __name__ == "__main__":
    print(FieldSH.F_REF)