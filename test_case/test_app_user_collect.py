from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """我的收藏"""

    def setUp(self):
        self.url = url + "/app/user/collect"

    def test_1(self):
        data = {'page': '',
                'userId': '',
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

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
