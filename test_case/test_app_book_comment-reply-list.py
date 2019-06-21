from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """回复列表"""

    def setUp(self):
        self.url = url + "/app/book/comment-reply-list"

    def test_1(self):
        data = {
            'book_id': '',
            'id': '',
            'page_num': ''
        }
        res = requests.get(url=self.url, params=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
