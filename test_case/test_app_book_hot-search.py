from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """热门搜索"""

    def setUp(self):
        self.url = url + "/app/book/hot-search"

    def test_1(self):
        data = {
            'page': '',
            'pagesize': '',
            'deviceid': '',
            'channel': '',
            'from': '',
            'version': '',
            'access_token': '',
            'access_type': '',
            'sign': ''
        }
        res = requests.post(url=self.url, params=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
