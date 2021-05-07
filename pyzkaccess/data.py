from enum import Enum
from pydantic import BaseModel


class DeviceParametersEnum(str, Enum):
    """all possible table names for device data"""

    serial_number = "serial_number"
    lock_count = "lock_count"
    reader_count = "reader_count"
    aux_in_count = "aux_in_count"
    aux_out_count = "aux_out_count"
    communication_password = "communication_password"
    ip_address = "ip_address"
    netmask = "netmask"
    gateway_ip_address = "gateway_ip_address"
    rs232_baud_rate = "rs232_baud_rate"
    watchdog_enabled = "watchdog_enabled"
    door4_to_door2 = "door4_to_door2"
    backup_hour = "backup_hour"
    reboot = "reboot"
    reader_direction = "reader_direction"
    fingerprint_version = "fingerprint_version"
    display_daylight_saving = "display_daylight_saving"
    enable_daylight_saving = "enable_daylight_saving"
    daylight_saving_mode = "daylight_saving_mode"

    anti_passback_rule = "anti_passback_rule"
    interlock = "interlock"
    spring_daylight_time_mode1 = "spring_daylight_time_mode1"
    fall_daylight_time_mode1 = "fall_daylight_time_mode1"
    spring_daylight_time_mode2 = "spring_daylight_time_mode2"
    fall_daylight_time_mode2 = "fall_daylight_time_mode2"


class TableName(str, Enum):
    """all possible table names for device data"""

    user = "user"
    userauthorize = "userauthorize"
    holiday = "holiday"
    timezone = "timezone"
    transaction = "transaction"
    firstcard = "firstcard"
    multimcard = "multimcard"
    inoutfun = "inoutfun"


# TODO: Discuss whether we should go with pydantic or not. since the rest of the pyzaccess library doesn't use pydantic.
class User(BaseModel):
    CardNo: int
    Pin: int
    Password: str
    Group: int
    StartTime: str
    EndTime: str
    SuperAuthorize: bool
