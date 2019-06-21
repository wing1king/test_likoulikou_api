from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """搜索"""

    def setUp(self):
        self.url = url + "/app/book/search"

    def test_1(self):
        data = {
            'search': '',
            'page': '',
            'pageSize': '',
            'deviceid': '',
            'channel': '',
            'from': '',
            'version': '',
            'access_token': '',
            'access_type': '',
            'sign': ''
        }
        res = requests.get(url=self.url, params=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
