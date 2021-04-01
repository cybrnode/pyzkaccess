from pyzkaccess.data import TableName
from pyzkaccess.exceptions import ZKSDKError
from pyzkaccess.device import ZK100
from pyzkaccess.pyzkaccess import ZKAccess

import pytest


class TestDeviceData:

    testUser = {
        "CardNo": "123456789",
        "Pin": "12345",
        "Password": "",
        "Group": "0",
        "StartTime": "0",
        "EndTime": "0",
        "SuperAuthorize": "0",
    }

    def setup(self):
        connstr = "protocol=TCP,ipaddress=192.168.10.201,port=4370,timeout=4000,passwd="

        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        # TODO: USE A MOCK ZkAccess DEVICE
        self.zk = ZKAccess(connstr=connstr, device_model=ZK100)

    def test_set_device_data_raises_no_exception(self):
        user = {
            "CardNo": "123456789",
            "Pin": "9999",
            "Password": "",
            "Group": "0",
            "StartTime": "0",
            "EndTime": "0",
            "SuperAuthorize": "0",
        }
        self.zk.sdk.set_device_data(TableName.user, [user])

    def test_set_data_with_user_data_should_add_non_existing_user_to_the_zk_device(self):
        # FIXME: THIS TEST IS POINTLESS UNTIL either A MOCK ZKAccess Device is implemented or delete_all_data is called in test setup
        # TODO: DO THIS FOR ALL TableNames, not only TableName.user

        self.zk.sdk.set_device_data(TableName.user, [self.testUser])

        users_data = self.zk.sdk.get_device_data(TableName.user, 1024 * 1024 * 4)

        user_found_in_device_data = False
        for i in users_data:
            print(i, self.testUser)
            if i.get("CardNo", "") != self.testUser.get("CardNo"):
                continue
            elif i.get("Pin", "") != self.testUser.get("Pin"):
                continue
            elif i.get("Password", "") != self.testUser.get("Password"):
                continue
            elif i.get("Group", "") != self.testUser.get("Group"):
                continue
            elif i.get("StartTime", "") != self.testUser.get("StartTime"):
                continue
            elif i.get("EndTime", "") != self.testUser.get("EndTime"):
                continue
            elif i.get("SuperAuthorize", "") != self.testUser.get("SuperAuthorize"):
                continue
            else:
                user_found_in_device_data = True
                break

        assert user_found_in_device_data is True

    def test_set_data_should_update_existing_user_in_the_zk_device(self):
        # TODO: DO THIS FOR ALL TableNames, not only TableName.user

        modifiedTestUser = self.testUser.copy()
        modifiedTestUser["Password"] = "PASSWORD"

        users_data = self.zk.sdk.get_device_data(TableName.user, 1024 * 1024 * 4)

        user_found_in_device_data = False
        for i in users_data:
            if i.get("CardNo", "") != modifiedTestUser.get("CardNo"):
                continue
            elif i.get("Pin", "") != modifiedTestUser.get("Pin"):
                continue
            elif i.get("Password", "") != modifiedTestUser.get("Password"):
                continue
            elif i.get("Group", "") != modifiedTestUser.get("Group"):
                continue
            elif i.get("StartTime", "") != modifiedTestUser.get("StartTime"):
                continue
            elif i.get("EndTime", "") != modifiedTestUser.get("EndTime"):
                continue
            elif i.get("SuperAuthorize", "") != modifiedTestUser.get("SuperAuthorize"):
                continue
            else:
                user_found_in_device_data = True
                break

        assert user_found_in_device_data is True

    def test_get_device_data_raises_no_exception(self):
        # buffer_size = 4 * 1024 * 1024
        for i in TableName:
            self.zk.get_data(i)

    def test_get_users_list_should_work_without_error(self):
        x = self.zk.get_users()
        print(x)

    def test_get_device_data_raises_exception_on_wrong_tablename(self):
        with pytest.raises(ZKSDKError):
            self.zk.sdk.get_device_data("!@*&$G^*OIL", 4 * 1024 * 1024)  # type: ignore
