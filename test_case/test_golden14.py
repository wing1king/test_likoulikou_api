from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """上传录音"""

    def setUp(self):
        self.url = url + "/gs-record/upload"

    def test_1(self):
        datas['gs_id'] = ''
        datas['record_url'] = ''
        datas['pub_status'] = ''    # 发布状态，1 发布，0不发布
        res = requests.post(url=self.url, data=datas)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
