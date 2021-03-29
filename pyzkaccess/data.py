from enum import Enum


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
