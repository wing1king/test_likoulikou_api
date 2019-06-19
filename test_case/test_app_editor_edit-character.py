from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """修改角色"""

    def setUp(self):
        self.url = url + "/app/editor/edit-character"

    def test_1(self):
        datas['book_id'] = ''
        datas['icon'] = ''
        datas['name'] = ''
        res = requests.post(url=self.url)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
