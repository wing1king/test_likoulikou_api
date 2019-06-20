from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """websocket链接"""

    def setUp(self):
        self.url = url + "/app/editor/ws"

    def test_1(self):
        data = {'book_id': '', 'chapter_id': ''}
        res = requests.get(url=self.url, params=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
