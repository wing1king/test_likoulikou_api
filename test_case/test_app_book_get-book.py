from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """评论列表"""

    def setUp(self):
        self.url = url + "/app/book/comment-list"

    def test_1(self):
        data = {'book_id': 1559790158063, 'type': 2}
        res = requests.get(url=self.url, params=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
