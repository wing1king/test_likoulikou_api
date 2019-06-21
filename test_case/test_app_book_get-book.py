from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """作品详情"""

    def setUp(self):
        self.url = url + "/app/book/get-book"

    def test_1(self):
        data = {
            'book_id': ''
        }
        res = requests.get(url=self.url, params=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
