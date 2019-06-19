from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """编辑器书本信息"""

    def setUp(self):
        self.url = url + "/app/editor/book"

    def test_1(self):
        datas['book_id']
        res = requests.get(url=self.url, params=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
