from tool.get_token import *

class MyTestCase(unittest.TestCase):
    """角色列表"""

    def setUp(self):
        self.url = url + "/app/editor/characters"

    def test_1(self):
        data = {'book_id':1559790158063}
        res = requests.get(url=self.url, params=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
