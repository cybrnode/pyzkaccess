from pyzkaccess.data import TableName, User
from pyzkaccess.exceptions import ZKSDKError
from pyzkaccess.device import ZK100
from pyzkaccess.pyzkaccess import ZKAccess

import pytest

# TODO: USE A MOCK ZkAccess DEVICE?
# TODO: USE A MOCK ZkAccess DEVICE?
# TODO: USE A MOCK ZkAccess DEVICE?
# TODO: USE A MOCK ZkAccess DEVICE?
# TODO: USE A MOCK ZkAccess DEVICE?
# TODO: USE A MOCK ZkAccess DEVICE?

# NOTE: This test will delete all data on the connected device.
test_device_connstr = "protocol=TCP,ipaddress=192.168.10.201,port=4370,timeout=4000,passwd="


class TestDeviceData:

    test_user_data = {
        "CardNo": "123456789",
        "Pin": "12345",
        "Password": "",
        "Group": "0",
        "StartTime": "0",
        "EndTime": "0",
        "SuperAuthorize": "0",
    }

    def delete_all_device_data(self):
        for tablename in TableName:
            device_data = self.zk.sdk.get_device_data(tablename, 1024 * 1024 * 4)
            for i in device_data:
                self.zk.sdk.delete_device_data(tablename, [i])

    def setup(self):
        # setup is called before each test in this class is run
        self.zk = ZKAccess(connstr=test_device_connstr, device_model=ZK100)
        self.delete_all_device_data()

        self.test_user = User(**self.test_user_data)

    def test_delete_all_device_data_deletes_newly_added_user_data(self):
        self.add_user_data_to_device(self.test_user_data)
        self.delete_all_device_data()

        assert not self.verify_user_data_found_in_device_data(self.test_user_data)
        assert len(list(self.get_users_data_using_sdk())) == 0

    def test_set_device_data_user_table_raises_no_exception(self):
        self.zk.sdk.set_device_data(TableName.user, [self.test_user_data])

    def verify_user_data_found_in_device_data(self, user_data):
        users_data = self.get_users_data_using_sdk()
        user_found_in_device_data = False

        for i in users_data:

            if i.get("CardNo", "") != user_data.get("CardNo"):
                continue
            elif i.get("Pin", "") != user_data.get("Pin"):
                continue
            elif i.get("Password", "") != user_data.get("Password"):
                continue
            elif i.get("Group", "") != user_data.get("Group"):
                continue
            elif i.get("StartTime", "") != user_data.get("StartTime"):
                continue
            elif i.get("EndTime", "") != user_data.get("EndTime"):
                continue
            elif i.get("SuperAuthorize", "") != user_data.get("SuperAuthorize"):
                continue
            else:
                user_found_in_device_data = True
                break

        return user_found_in_device_data

    def test_set_data_with_user_data_should_add_non_existing_user_to_the_zk_device(self):
        self.add_test_user_to_device()
        assert self.verify_user_data_found_in_device_data(self.test_user_data) is True

    def get_users_data_using_sdk(self):
        users_data = self.zk.sdk.get_device_data(TableName.user, 1024 * 1024 * 4)
        return users_data

    def add_test_user_to_device(self):
        self.add_user_data_to_device(self.test_user_data)

    def add_user_data_to_device(self, user_data):
        self.zk.sdk.set_device_data(TableName.user, [user_data])

    def test_set_data_user_table_should_update_existing_user_in_the_zk_device(self):
        self.add_test_user_to_device()

        modified_test_user = self.test_user_data.copy()
        modified_test_user["Password"] = "12345"
        modified_test_user["Group"] = "2"

        self.zk.sdk.set_device_data(TableName.user, [modified_test_user])
        assert self.verify_user_data_found_in_device_data(modified_test_user)

    def test_get_device_data_raises_no_exception(self):
        for i in TableName:
            self.zk.get_data(i)

    def test_get_users_list_should_work_without_error(self):
        self.zk.get_users()

    def test_get_users_should_return_the_added_user(self):

        added_user = User(**self.test_user_data)
        self.zk.add_users([added_user])

        assert added_user in self.zk.get_users()

    def test_get_users_should_return_multiple_added_user(self):
        new_user_1_data = {**self.test_user_data, "Pin": "1"}
        new_user_2_data = {**self.test_user_data, "Pin": "2"}
        new_user_3_data = {**self.test_user_data, "Pin": "3"}

        new_user_1 = User(**new_user_1_data)
        new_user_2 = User(**new_user_2_data)
        new_user_3 = User(**new_user_3_data)

        self.zk.add_users([new_user_1])
        self.zk.add_users([new_user_2])
        self.zk.add_users([new_user_3])

        assert new_user_1 in self.zk.get_users()
        assert new_user_2 in self.zk.get_users()
        assert new_user_3 in self.zk.get_users()

        not_new_user_4_data = {**self.test_user_data, "Pin": "4"}
        not_new_user_4 = User(**not_new_user_4_data)

        assert not_new_user_4 not in self.zk.get_users()

    def test_get_device_data_raises_exception_on_wrong_tablename(self):
        with pytest.raises(ZKSDKError):
            self.zk.sdk.get_device_data("!@*&$G^*OIL", 4 * 1024 * 1024)  # type: ignore
