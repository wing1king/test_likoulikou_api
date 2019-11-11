from tool.get_token import *

class MyTestCae(unittest.TestCase):
    """打赏"""
    def Setup(self):
        self.user_id = 99999999999
        self.gift_id = ""
        self.count = ""
        self.item_id = ""
        self.item_type = 0      # 0是指定角色送礼；1是没有指定角色填
        self.room_id = ""
        self.begin_time = ""
        self.end_time = ""
        self.hot_id = ""
        self.hot_type = ""

    def test_get_gift_list(self):
        """获取用户礼物"""
        data = {
            "user_id": self.user_id,
        }
        res = requests.post(url=base_url + "/app/gift/get-gift-list",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_send_gift(self):
        """送礼物"""
        data = {
            "user_id": self.user_id,
            "gift_id": self.gift_id,
            "count": self.count,
            "item_id": self.item_id,
            "item_type": self.item_type,
            "room_id": self.room_id,
        }
        res = requests.post(url=base_url + "/app/gift/send-gift",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_contribution_list(self):
        """获取贡献排行"""
        data = {
            "item_id": self.item_id,
            "page_num": 1,
            "page_size": 5,
            "item_type": 0,      # 0是角色，1是房间
        }
        res = requests.post(url=base_url + "/app/gift/get-contribution-list",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_gift_history(self):
        """获取用户消费历史"""
        data = {
            "user_id": self.user_id,
            "begin_time": self.begin_time,
            "end_time": self.end_time,
            "page_num": 1,
            "page_size": 5,
        }
        res = requests.post(url=base_url + "/app/gift/get-gift-history",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_item_contribution_list(self):
        """获取总贡献排行榜"""
        data = {
            "user_id": ""
        }
        res = requests.post(url=base_url + "/app/gift/get-item-contribution-list",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_send_hot(self):
        """发送热度礼物"""
        data = {
            "user_id": self.user_id,
            "hot_id": self.hot_id,
            "hot_type": self.hot_type,
            "count": self.count,
            "room_id": self.room_id
        }
        res = requests.post(url=base_url + "/app/gift/send-hot",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
