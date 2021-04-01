from enum import Enum
from pydantic import BaseModel


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
