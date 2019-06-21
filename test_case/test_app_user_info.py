from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """"""

    def setUp(self):
        self.url = url + "/app/user/info"

    def test_1(self):
        data = {'userId': '',
                'deviceid': '',
                'channel': '',
                'from': '', # 1是安卓 2是IOS 3其他
                'version': '',
                'access_token': '',
                'access_type': '2',  # 1游客 2用户
                'sign': ''}
        res = requests.post(url=self.url, json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
