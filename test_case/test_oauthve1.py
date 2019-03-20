from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """刷新token"""

    def setUp(self):
        self.url = url + "/oauth/verify-token"

    def test_1(self):
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
