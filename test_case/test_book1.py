from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """ 书数据获取"""

    def setUp(self):
        self.url = url + "/book/get-data"

    def test_1(self):
        datas['bookId'] = get_book_id()
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"操作成功" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
