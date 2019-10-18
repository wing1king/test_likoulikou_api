from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """作品评论"""

    def setUp(self):

        self.item_id = 0
        self.page_num = 1
        self.page_size = 5
        # 10004-钱过敏
        self.user_id = 10004
        # 70648311677614-怎么办！那个女孩的毛发太旺盛！
        self.book_id = 70648311677614

    def test_add_comment(self):
        """添加评论"""
        data = {
            "item_id": self.item_id,
            "item_type": 0, # 0：书本，1：章节对话体，2：活动，3：广场
            "item_meta": 2,
            "content" : "123654",
            "author_id": self.user_id
        }
        res = requests.post(url=base_url + "/app/comment/add-comment",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_comment(self):
        """删除评论"""
        data = {
            "item_id": self.item_id,
            "item_type": "",
            "comment_id": ""
        }
        res = requests.post(url=base_url + "/app/comment/del-comment", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_comments(self):
        """评论列表"""
        data = {
            "item_id": self.item_id,
            "list_type": 0, # 0：默认，1：精评
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/comment/get-comments", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_reply(self):
        """添加回复"""
        data = {
            "item_id": self.item_id,
            "list_type": 0, # 0：默认，1：精评
            "comment_id": "",
            "content": "",
            "reply_to_user_id": "",
            "parent_reply_id": "",
            "author_id": ""
        }
        res = requests.post(url=base_url + "/app/comment/add-reply", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_reply(self):
        """删除回复"""
        data = {
            "book_id": self.book_id,
            "comment_id": "",
            "comment_reply_id": ""
        }
        res = requests.post(url=base_url + "/app/comment/del-reply", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_replies(self):
        """回复列表"""
        data = {
            "book_id": self.book_id,
            "id": "",
            "page_num": self.page_num
        }
        res = requests.post(url=base_url + "/app/comment/get-replies", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_like(self):
        """添加点赞"""
        data = {
            "item_id": self.item_id,
            "item_type": "",
            "author_id": ""
        }
        res = requests.post(url=base_url + "/app/comment/add-like", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_like(self):
        """取消点赞"""
        data = {
            "item_id": self.item_id,
            "item_type": ""
        }
        res = requests.post(url=base_url + "/app/comment/del-like", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
