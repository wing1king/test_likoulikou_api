from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """评论回复"""

    def setUp(self):
        self.url = url + "/app/book/comment-reply-add"

    def test_1(self):
        data = {
            'comment_id': '',
            'book_id': '',
            'content': '',
            'reply_to_user_id': '',
            'parent_reply_id': ''
        }
        res = requests.post(url=self.url, json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
