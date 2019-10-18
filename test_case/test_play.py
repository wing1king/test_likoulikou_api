from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """游戏数据"""

    def setUp(self):
        pass

    def test_vote(self):
        """用户投票"""
        data = {
            "book_id": "",
            "chapter_id": "",
            "cmd_id": "",
            "option_id": ""
        }
        res = requests.post(url=base_url + "/app/play/vote", headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_clear_vote(self):
        """清除投票结果"""
        data = {
            "book_id": "",
            "chapter_id": "",
            "cmd_id": "",
            "option_id": ""
        }
        res = requests.post(url=base_url + "/app/play/clear-vote", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_vote_data(self):
        """获取投票结果数据"""
        data = {
            "book_id": "",
            "chapter_id": "",
            "cmd_id": ""
        }
        res = requests.post(url=base_url + "/app/play/vote-data", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_data(self):
        """获取游戏存储数据"""
        data = {
            "book_id": "",
            "data_key": ""
        }
        res = requests.post(url=base_url + "/app/play/get-data", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_set_data(self):
        """设置游戏存储数据"""
        data = {
            "book_id": "",
            "data": ""
        }
        res = requests.post(url=base_url + "/app/play/set-data", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_data(self):
        """删除游戏存储数据"""
        data = {
            "book_id": "",
            "data_key": ""
        }
        res = requests.post(url=base_url + "/app/play/del-data", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
