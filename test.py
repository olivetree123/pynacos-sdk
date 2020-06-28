import time
from nacos.nacos import Nacos
from nacos.entities import (LoginResponse, RoleListResponse,
                            PermissionListResponse)

NACOS_HOST = "10.88.190.154"
NACOS_PORT = 8848
NAMESPACE_ID = "e26e7439-e161-4709-8778-ab5ecef5fec5"

USERNAME = "olivetree2"
PASSWORD = "123456"
ROLE = "normal_user"

nacos_client = Nacos(NACOS_HOST, NACOS_PORT, NAMESPACE_ID)


class TestNacos(object):
    def test_user_create(self):
        r = nacos_client.user_create(username=USERNAME, password=PASSWORD)
        assert r == True

    def test_user_update(self):
        r = nacos_client.user_update(username=USERNAME,
                                     old_password=PASSWORD,
                                     new_password=PASSWORD + "1")
        assert r == True

    def test_user_delete(self):
        r = nacos_client.user_delete(username=USERNAME, password=PASSWORD)
        assert r == True

    def test_login(self):
        r = nacos_client.login(username=USERNAME, password=PASSWORD)
        assert isinstance(r, LoginResponse)

    def test_role_create(self):
        r = nacos_client.role_create(username=USERNAME, role=ROLE)
        assert r == True

    def test_role_list(self):
        r = nacos_client.role_list(username=USERNAME)
        assert isinstance(r, RoleListResponse)

    def test_role_delete(self):
        r = nacos_client.role_delete(username=USERNAME, role=ROLE)
        assert r == True

    def permission_add(self):
        r = nacos_client.permission_add(role=ROLE,
                                        resource="image",
                                        action="write")
        assert r == True

    def permission_list(self):
        r = nacos_client.permission_list(role=ROLE)
        assert isinstance(r, PermissionListResponse)

    def permission_delete(self):
        r = nacos_client.permission_delete(role=ROLE,
                                           resource="image",
                                           action="write")
        assert r == True


if __name__ == "__main__":
    t = TestNacos()
    try:
        # 用户管理
        t.test_user_create()
        time.sleep(10)
        t.test_login()

        # 角色管理
        t.test_role_create()
        t.test_role_list()

        # 权限管理
        t.permission_add()
        t.permission_list()
    except Exception as e:
        print(e)
    finally:
        # 清理测试数据
        t.test_user_delete()
        t.test_role_delete()
        t.permission_delete()
