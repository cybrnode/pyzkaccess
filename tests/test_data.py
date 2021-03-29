from pyzkaccess.data import TableName
from pyzkaccess.exceptions import ZKSDKError
from pyzkaccess.device import ZK100
from pyzkaccess.pyzkaccess import ZKAccess
from pprint import pprint

import pytest


class UserTableData:
    CardNo = ""
    Pin = ""
    Password = ""
    Group = ""
    StartTime = ""
    EndTime = ""
    SuperAuthorize = ""

    def __init__(self, CardNo="", Pin="", Password="", Group="", StartTime="", EndTime="", SuperAuthorize="") -> None:
        pass


class TestIDK:
    def setup(self):
        connstr = "protocol=TCP,ipaddress=192.168.10.201,port=4370,timeout=4000,passwd="
        self.zk = ZKAccess(connstr=connstr, device_model=ZK100)
        print("Device SN:", self.zk.parameters.serial_number, "IP:", self.zk.parameters.ip_address)

    def test_set_device_data_raises_no_exception(self):
        x = {
            'CardNo': '15540203',
            'Pin': '1',
            'Password': '123',
            'Group': '0',
            'StartTime': '0',
            'EndTime': '0',
            'SuperAuthorize': '1'
        }
        self.zk.sdk.set_device_data(TableName.user, [x])

    def test_get_device_data_raises_no_exception(self):
        # buffer_size = 4 * 1024 * 1024
        pprint(self.zk.get_data(TableName.user))
        for i in TableName:
            self.zk.get_data(i)

    def test_get_device_data_raises_exception_on_wrong_tablename(self):
        with pytest.raises(ZKSDKError):
            ret = self.zk.sdk.get_device_data('!@*&$G^*OIL', 4 * 1024 * 1024)
            print(ret)
