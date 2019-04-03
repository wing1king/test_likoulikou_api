from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """根据话题录音id获取录音话题信息"""

    def setUp(self):
        self.url = url + "/gs-record/topic-info"

    def test_1(self):
        datas['business_id'] = ''
        datas['topic_id'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
