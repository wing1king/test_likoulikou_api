from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """活动预约"""

    def setUp(self):
        self.url = url + "/activity-h5/book"

    def test_1(self):
        """参数为空"""
        datas['key'] = ''
        datas['mobile'] = ''
        datas['code'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"手机号码不正确或验证码错误" in res.text)

    def test_2(self):
        """错误参数"""
        datas['key'] = 'jxb_book1'
        datas['mobile'] = '185656677888'
        datas['code'] = '122324564'
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"未找到该活动" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
