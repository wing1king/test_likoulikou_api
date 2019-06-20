from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """删除角色"""

    def setUp(self):
        self.url = url + "/app/editor/del-character"

    def test_1(self):
        data = {'book_id': '', 'character_id': ''}
        res = requests.post(url=self.url, json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
