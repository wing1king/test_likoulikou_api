from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """问题收集"""

    def setUp(self):
        self.url = url + "/activity/issue-save"

    def test_1(self):
        """正确传参"""
        datas['gameId'] = get_gameId()
        datas['content'] = ''
        datas['attr'] = ''
        datas['title'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)
        # self.assertEqual("操作成功", "操作成功")

    def test_2(self):
        """参数为空"""
        datas['gameId'] = ''
        datas['content'] = ''
        datas['attr'] = ''
        datas['title'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"参数缺失" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
