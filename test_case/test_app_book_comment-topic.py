from tool.get_token import *

class MyTestCase(unittest.TestCase):
    """评论和回复"""

    def setUp(self):
        self.url = url + "/app/book/comment-topic"

    def test_1(self):
        data = {'topicId': '',
                'book_id':1560153642454,
                'content': '',
                'replyToTopicUserId': '',
                'commentId': '',
                'replyToCommentUserId': ''}
        res = requests.post(url=self.url, json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
