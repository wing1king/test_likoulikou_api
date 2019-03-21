from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """获取活动页分享信息"""

    def setUp(self):
        self.url = url + "/activity-h5/get-share-info"

    def test_1(self):
        """正确传参"""
        datas['key'] = 'jxb_book'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def test_2(self):
        """参数错误"""
        datas['key'] = 'jxb_book1'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def test_3(self):
        """参数为空"""
        datas['key'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"参数错误" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()