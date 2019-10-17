from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """评论书本"""

    def setUp(self):
        self.url = url + "/app/book/comment-book"

    def test_1(self):
        data = {
            'bookId': '',
            'content': ''
        }
        res = requests.post(url=self.url, json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
