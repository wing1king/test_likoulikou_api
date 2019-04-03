from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """删除录音"""

    def setUp(self):
        self.url = url + "/gs-record/del"

    def test_1(self):
        datas['gs_id'] = ''
        datas['id'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
