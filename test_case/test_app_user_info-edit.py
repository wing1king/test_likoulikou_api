from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """编辑个人信息"""
    @classmethod
    def setUpClass(cls):
        cls.url = url + "/app/user/info-edit"

    def test_1(self):
        """头像更换"""
        data = {'avatar': '',
                'deviceid': '',
                'channel': '',
                'from': '',
                'version': '',
                'access_token': '',
                'access_type': '',
                'sign': ''}
        res = requests.post(url=self.url, json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_2(self):
        """背景更换"""
        data = {'bgImg': '',
                'deviceid': '',
                'channel': '',
                'from': '',
                'version': '',
                'access_token': '',
                'access_type': '',
                'sign': ''}
        res = requests.post(url=self.url, json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_3(self):
        """昵称更换"""
        data = {'nickName': '',
                'deviceid': '',
                'channel': '',
                'from': '',
                'version': '',
                'access_token': '',
                'access_type': '',
                'sign': ''}
        res = requests.post(url=self.url, json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
