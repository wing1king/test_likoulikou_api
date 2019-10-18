from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """作品评论"""

    def setUp(self):
        self.page_num = 1
        self.page_size = 5
        # 10004-钱过敏
        self.user_id = 10004
        # 70648311677614-怎么办！那个女孩的毛发太旺盛！
        self.book_id = 70648311677614

    def test_add_comment(self):
        """添加评论"""
        data = {
            "item_id": self.book_id,
            "item_type": 0, # 0：书本，1：章节对话体，2：活动，3：广场
            "item_meta": {},
            "content" : "123654",
            "author_id": self.user_id
        }
        res = requests.post(url=base_url + "/app/comment/add-comment",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)
        return res.json()['data']['id']


    def test_del_comment(self):
        """删除评论"""
        data = {
            "item_id": self.book_id,
            "item_type": 0,
            "comment_id": self.test_add_comment()
        }
        res = requests.post(url=base_url + "/app/comment/del-comment", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_comments(self):
        """评论列表"""
        data = {
            "item_id": self.book_id,
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
            "item_id": self.book_id,
            "list_type": 0, # 0：默认，1：精评
            "comment_id": 128641000267776,
            "content": "123",
            "reply_to_user_id": 2367568746,
            "parent_reply_id": 132503382933504,
            "author_id": 1
        }
        res = requests.post(url=base_url + "/app/comment/add-reply", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_reply(self):
        """删除回复"""
        data = {
            "book_id": self.book_id,
            "comment_id": 1,
            "comment_reply_id": 0
        }
        res = requests.post(url=base_url + "/app/comment/del-reply", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_replies(self):
        """回复列表"""
        data = {
            "book_id": self.book_id,
            "id": 1,
            "page_num": self.page_num
        }
        res = requests.post(url=base_url + "/app/comment/get-replies", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_like(self):
        """添加点赞"""
        data = {
            "item_id": self.book_id,
            "item_type": 0,
            "author_id": 132503382933504
        }
        res = requests.post(url=base_url + "/app/comment/add-like", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_like(self):
        """取消点赞"""
        data = {
            "item_id": self.book_id,
            "item_type": ""
        }
        res = requests.post(url=base_url + "/app/comment/del-like", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
