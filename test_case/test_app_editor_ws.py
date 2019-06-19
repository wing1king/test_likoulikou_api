from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """websocket链接"""

    def setUp(self):
        self.url = url + "/app/editor/ws"

    def test_1(self):
        datas['book_id'] = ''
        datas['chapter_id'] = ''
        res = requests.get(url=self.url, params=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
