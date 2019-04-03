from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """根据id获取录音列表"""

    def setUp(self):
        self.url = url + "/gs-record/listr"

    def test_1(self):
        datas['gs_id'] = ''
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
