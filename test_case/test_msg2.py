from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """我的消息-回复我的"""

    def setUp(self):
        self.url = url + "/msg/reply"

    def test_1(self):
        datas['page'] = 1
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
