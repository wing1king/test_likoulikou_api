from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """用户"""

    def setUp(self):
        self.user_id = 99999999999
        self.page_num = 1
        self.page_size = 5

    def test_report(self):
        """投拆"""
        data = {
            "book_id": 129337698467840,
            "user_id": self.user_id,
            "reason_id": 4
        }
        res = requests.post(url= base_url + "/app/user/report",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_login(self):
        """登录/注册"""
        data = {
            'openid': "164b4571e4542ca8f2cc19776f7fd2f211111",
            'uid': 99999999999,	# 170****2087手机号
            'sessionid': "a9d384dd8ca7a22ec38505ddaf03eb6605b6a62661",
        }
        res = requests.post(url= base_url + '/app/user/login', json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_refresh_token(self):
        """刷新token"""
        res = requests.post(url= base_url + "/app/user/refresh-token", headers=headers)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_books(self):
        """书本列表"""
        data = {
            "user_id": self.user_id,
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url= base_url + "/app/user/books", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_profile(self):
        """设置个人数据"""
        data = {
            "nick_name": "wingking",
            "avatar": "https://xms-dev-1251001060.cos.ap-guangzhou.myqcloud.com/2019/09/1568086837108.jpg"
        }
        res = requests.post(url=base_url + "/app/user/edit-profile", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_profile(self):
        """获取个人页数据"""
        data = {
            "user_id": self.user_id
        }
        res = requests.post(url=base_url + "/app/user/get-profile", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_black_list(self):
        """获取黑名单列表"""
        data = {
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/user/get-black-list", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_black_list(self):
        """将用户加入黑名单"""
        data = {
            "report_user_id": 2377315028
        }
        res = requests.post(url=base_url + "/app/user/add-black-list", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_cancel_black_list(self):
        """将用户移出黑名单"""
        data = {
            "report_user_id": 2377315028
        }
        res = requests.post(url=base_url + "/app/user/cancel-black-list", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_black_list1(self):
        """获取黑名单中指定用户"""
        data = {
            "report_user_id": 2377315028
        }
        res = requests.post(url=base_url + "/app/user/get-black-list", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_cos_auth(self):
        """获取COS临时参数"""
        res = requests.post(url=base_url + "/app/user/get-cos-auth", headers=headers)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
