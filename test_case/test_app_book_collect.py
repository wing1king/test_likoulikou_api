from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """添加收藏"""

    def setUp(self):
        self.url = url + "/app/book/collect"

    def test_1(self):
        data = {
            'book_id': '',
            'type': ''  # 0:收藏，1：取消收藏
        }
        res = requests.get(url=self.url, params=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
