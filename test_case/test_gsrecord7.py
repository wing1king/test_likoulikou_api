from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """评论话题和回复评论"""

    def setUp(self):
        self.url = url + "/gs-record/topic-comment"

    def test_1(self):
        datas['topic_id'] = ''
        datas['business_id'] = ''
        datas['content'] = ''
        datas['reply_to_topic_user_id'] = ''
        datas['comment_id'] = ''
        datas['reply_to_comment_user_d'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
