from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """模板"""

    def setUp(self):
        pass

    def test_book_tile(self):
        """书籍单元"""
        res = requests.post(url=base_url + "/app/book/tile",headers=headers)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_comment_tile(self):
        """评论单元"""
        res = requests.post(url=base_url + "/app/comment/tile",headers=headers)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_reply_tile(self):
        """回复单元"""
        res = requests.post(url=base_url + "/app/reply/tile",headers=headers)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
