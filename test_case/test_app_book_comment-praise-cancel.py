from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """取消评论点赞"""

    def setUp(self):
        self.url = url + "/app/book/comment-praise-cancel"

    def test_1(self):
        data = {
            'book_id': '',
            'comment_id': ''
        }
        res = requests.post(url=self.url, json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
