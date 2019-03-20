from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """首页"""

    def setUp(self):
        self.url = url + "/home/index"

    def test_1(self):
        datas['page'] = 1
        datas['pageSize'] = 10
        datas['orderTime'] = ''
        datas['weight'] = ''
        datas['handle'] = ''
        datas['gameId'] = ''
        datas['all'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
