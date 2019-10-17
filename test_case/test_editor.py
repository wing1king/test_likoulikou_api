from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """评论列表"""

    def setUp(self):
        self.url = url + "/app/book/comment-list"

    def test_1(self):
        data = {
            'bookId': '',
            'type': '',     # 1：精评，2：所有评论
            'page': ''
        }
        res = requests.get(url=self.url, params=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
