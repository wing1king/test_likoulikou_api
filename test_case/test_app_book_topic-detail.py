from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """获取评论详情"""

    def setUp(self):
        self.url = url + "/app/book/topic-detail"

    def test_1(self):
        data = {
            'bookId': '',
            'topicId': ''
        }
        res = requests.get(url=self.url, params=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
