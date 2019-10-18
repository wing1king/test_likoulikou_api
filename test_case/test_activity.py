from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """活动"""

    def setUp(self):
        self.page_num = 1
        self.page_size = 5
        self.user_id = ""

    def test_create_activity(self):
        """创建活动"""
        data = {
            "tag_name": "",
            "title": "",
            "start_time": "",
            "end_time": "",
            "home_image": "",
            "tag_image": "",
            "position": "",
            "content": ""
        }
        res = requests.post(url=base_url + "/app/activity/create-activity",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_activity(self):
        """编辑活动"""
        data = {
            "activity_id": "",
            "tag_name": "",
            "title": "",
            "start_time": "",
            "end_time": "",
            "home_image": "",
            "tag_image": "",
            "position": "",
            "content": ""
        }
        res = requests.post(url=base_url + "/app/activity/edit-activity",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_edit_shared(self):
        """编辑活动分享"""
        data = {
            "activity_id": "",
            "shared_title": "",
            "shared_intro": "",
            "shared_image": ""
        }
        res = requests.post(url=base_url + "/app/activity/edit-shared",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_discovery_activity(self):
        """获取首页发现活动列表"""
        data = {
            "page_num": self.page_num,
            "page_size": self.page_size,
            "user_id": ""
        }
        res = requests.post(url=base_url + "/app/activity/get-discovery-activity",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_activity_introduce_info(self):
        """获取活动介绍页"""
        data = {
            "user_id": "",
            "activity_id": ""
        }
        res = requests.post(url=base_url + "/app/activity/get-activity-introduce-info",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_activity_detail(self):
        """获取活动介绍页"""
        data = {
            "user_id": "",
            "activity_id": ""
        }
        res = requests.post(url=base_url + "/app/activity/get-activity-detail",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_activity_praise(self):
        """点赞活动"""
        data = {
            "user_id": "",
            "activity_id": ""
        }
        res = requests.post(url=base_url + "/app/activity/add-activity-praise", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_activity_praise(self):
        """取消点赞"""
        data = {
            "user_id": "",
            "activity_id": ""
        }
        res = requests.post(url=base_url + "/app/activity/del-activity-praise", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_activity_tags(self):
        """获取当前所有活动标签"""
        data = {
            "user_id": "",
            "activity_id": ""
        }
        res = requests.post(url=base_url + "/app/activity/get-activity-tags", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_shared(self):
        """获取活动分享信息"""
        data = {
            "user_id": "",
            "activity_id": ""
        }
        res = requests.post(url=base_url + "/app/activity/get-shared", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
