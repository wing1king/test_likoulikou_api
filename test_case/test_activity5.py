from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """问题收集配置"""

    def setUp(self):
        self.url = url + "/activity/issue-config"

    def test_1(self):
        """正确传参"""
        datas['gameId'] = get_gameId()
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def test_2(self):
        """参数错误"""
        datas['gameId'] = '1'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_3(self):
        """参数为空"""
        datas['gameId'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"参数缺失" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
