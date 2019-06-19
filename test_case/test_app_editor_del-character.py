from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """删除角色"""

    def setUp(self):
        self.url = url + ""

    def test_1(self):
        res = requests.post(url=self.url)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
