from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """广场帖子"""

    def setUp(self):
        self.page_num = 1
        self.page_size = 5
        self.user_id = ""

    def test_create_topic(self):
        """创建帖子"""
        data = {
            "title": "",
            "content": "",
            "home_image": "",
            "link_book_id": "",
            "topic_type": "",
            "background": "",
            "image_width": "",
            "image height": ""
        }
        res = requests.post(url=base_url + "/app/plaza/create-topic",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_del_topic(self):
        """删除帖子"""
        data = {
            "user_id": "",
            "topic_id": ""
        }
        res = requests.post(url=base_url + "/app/plaza/del-topic",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_edit_topic(self):
        """编辑帖子"""
        data = {
            "topic_id": "",
            "title": "",
            "content": "",
            "home_image": "",
            "link_book_id": ""
        }
        res = requests.post(url=base_url + "/app/plaza/edit-topic",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_(self):
        """获取广场帖子列表"""
        data = {
            "book_id": "",
            "id": "",
            "page_num": ""
        }
        res = requests.post(url=base_url + "/app/plaza/get-plaza-list",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_(self):
        """获取帖子详情"""
        data = {
            "book_id": "",
            "id": "",
            "page_num": ""
        }
        res = requests.post(url=base_url + "/app/plaza/get-topic-info",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_(self):
        """获取帖子评论列表"""
        data = {
            "book_id": "",
            "id": "",
            "page_num": ""
        }
        res = requests.post(url=base_url + "/app/plaza/get-topic-comment-list",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_(self):
        """获取评论回复列表"""
        data = {
            "book_id": "",
            "id": "",
            "page_num": ""
        }
        res = requests.post(url=base_url + "/app/plaza/get-comment-reply-list",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_(self):
        """删除帖子评论"""
        data = {
            "book_id": "",
            "id": "",
            "page_num": ""
        }
        res = requests.post(url=base_url + "/app/plaza/del-topic-comment",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_(self):
        """添加帖子评论"""
        data = {
            "book_id": "",
            "id": "",
            "page_num": ""
        }
        res = requests.post(url=base_url + "/app/plaza/add-topic-comment",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_(self):
        """添加评论回复"""
        data = {
            "book_id": "",
            "id": "",
            "page_num": ""
        }
        res = requests.post(url=base_url + "/app/plaza/add-topic-comment-reply",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_(self):
        """删除评论回复"""
        data = {
            "book_id": "",
            "id": "",
            "page_num": ""
        }
        res = requests.post(url=base_url + "/app/plaza/del-comment-reply",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_add_topic_praise(self):
        """点赞帖子"""
        data = {
            "topic_id": 1
        }
        res = requests.post(url=base_url + "/app/plaza/add-topic-praise",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_del_topic_praise(self):
        """取消帖子点赞"""
        data = {
            "topic_id": 1
        }
        res = requests.post(url=base_url + "/app/plaza/del-topic-praise",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_add_topic_comment_praise(self):
        """点赞评论"""
        data = {
            "comment_id": 1
        }
        res = requests.post(url=base_url + "/app/plaza/add-topic-comment-praise",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_del_topic_comment_praise(self):
        """取消评论点赞"""
        data = {
            "comment_id": 1
        }
        res = requests.post(url=base_url + "/app/plaza/del-topic-comment-praise",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_add_topic_comment_reply_praise(self):
        """点赞回复"""
        data = {
            "reply_id": 1
        }
        res = requests.post(url=base_url + "/app/plaza/add-topic-comment-reply-praise",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_del_topic_comment_reply_praise(self):
        """取消回复点赞"""
        data = {
            "reply_id": 1
        }
        res = requests.post(url=base_url + "/app/plaza/del-topic-comment-reply-praise",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_get_exquisite_comment(self):
        """获取精品评论"""
        data = {
            "book_id": "",
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/plaza/get-exquisite-comment",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_get_book_link_topic_list(self):
        """获取书本关联帖子列表"""
        data = {
            "book_id": "",
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/plaza/get-book-link-topic-list",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def test_get_user_topics(self):
        """获取用户帖子"""
        data = {
            "user_id": self.user_id,
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/plaza/get-user-topics",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
