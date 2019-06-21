from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """举报评论"""

    def setUp(self):
        self.url = url + "/app/book/report-comment"

    def test_1(self):
        data = {
            'reportUserId': '',
            'bookId': '',
            'topicId': '',
            'commentId': '',
            'reasonContent': ''
        }
        res = requests.post(url=self.url, json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
