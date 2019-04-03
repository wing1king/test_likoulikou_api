from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """录音话题评论列表"""

    def setUp(self):
        self.url = url + "/gs-record/topic-comment-list"

    def test_1(self):
        datas['business_id'] = ''
        datas['topic_id'] = ''
        datas['page'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
