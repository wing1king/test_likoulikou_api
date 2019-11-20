from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """打赏"""
    def setUp(self):
        self.user_id = 99999999999
        self.activity_id = 133796910956544
        self.user_mobile = ""
        self.act_key = "ActivityDRJL"

    def test_get_activity(self):
        """获取活动"""
        data = {
            "act_key": self.act_key,
        }
        res = requests.post(url=base_url + "/app/extend/get-activity",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_user_data(self):
        """获取用户活动数据"""
        data = {
            "activity_id": self.act_key,
        }
        res = requests.post(url=base_url + "/app/extend/get-user-data",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_test_topic(self):
        """获取测试题"""
        data = {
            "activity_id": self.activity_id,
        }
        res = requests.post(url=base_url + "/app/extend/get-test-topic",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_lottery_draw(self):
        """抽奖接口"""
        data = {
            "activity_id": self.activity_id,
        }
        res = requests.post(url=base_url + "/app/extend/lottery-draw",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_recode(self):
        """兑换礼物"""
        data = {
            "activity_id": self.activity_id,
            "user_mobile": self.user_mobile,
            "user_name": "",
            "user_addr": "",
        }
        res = requests.post(url=base_url + "/app/extend/recode", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_subscribe(self):
        """预约"""
        data = {
            "activity_id": self.activity_id,
            "user_mobile": self.user_mobile,
            "verify": "",
        }
        res = requests.post(url=base_url + "/app/extend/subscribe", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_unlock_character(self):
        """解锁角色"""
        data = {
            "activity_id": self.activity_id,
        }
        res = requests.post(url=base_url + "/app/extend/unlock-character", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """发送短信"""
        data = {
            "user_mobile": self.user_mobile,
        }
        res = requests.post(url=base_url + "/app/extend/get-code", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
