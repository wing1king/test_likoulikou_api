from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """举报评论、话题"""

    def setUp(self):
        self.url = url + "/gs-record/comment-report"

    def test_1(self):
        datas['report_user_id'] = ''
        datas['business_id'] = ''
        datas['topic_id'] = ''
        datas['comment_id'] = ''
        datas['reason_content'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
