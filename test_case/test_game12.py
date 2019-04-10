from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """Premium选项扣费"""

    def setUp(self):
        self.url = url + "/game/premium"

    def test_1(self):
        datas['gameId'] = get_gameId()
        datas['chapterId'] = '1538998937488'
        datas['optionType'] = 'fed4d9f4-b042-4225-bb62-745bff4dea08'
        datas['optionId'] = 'qqqq'
        datas['type'] = 'VCKEY'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
