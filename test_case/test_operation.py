from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """公共"""

    def setUp(self):
        pass

    def test_get_report(self):
        """获取举报类型"""
        res = requests.post(url=base_url + "/app/operation/get-report", headers=headers)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_version(self):
        """获取最新版本号"""
        res = requests.post(url=base_url + "/app/operation/version", headers=headers)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_carousels(self):
        """获取轮播海报"""
        data = {
            "set": ""
        }
        res = requests.post(url=base_url + "/app/operation/get-carousels", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
