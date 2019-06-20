from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """上传文件"""

    def setUp(self):
        self.url = url + "/app/upload"

    def test_1(self):
        files = {'file': open(r'E:/banner5.png', 'rb')}
        res = requests.post(url=self.url, files=files)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
