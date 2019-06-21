from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """评论点赞"""

    def setUp(self):
        self.url = url + "/app/book/praise-topic"

    def test_1(self):
        data = {
            'bookid': '',
            'topicId': '',
            'type': ''  # 1:点赞，2：取消点赞
        }
        res = requests.post(url=self.url, json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
