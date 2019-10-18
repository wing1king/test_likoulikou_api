from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """章节评论"""

    def setUp(self):
        self.page_num = 1
        self.page_size = 5
        self.user_id = ""

    def test_comment_list(self):
        """获取章节评论列表"""
        data = {
            "book_id": "",
            "chapter_id": "",
            "cmd_id": "",
            "type": "",
            "page_num": ""
        }
        res = requests.post(url=base_url + "/app/chapter/comment-list", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_comment_del(self):
        """删除章节评论"""
        data = {
            "book_id": "",
            "chapter_id": "",
            "cmd_id": "",
            "type": "",
            "page_num": ""
        }
        res = requests.post(url=base_url + "/app/chapter/comment-del", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_chapter_comment(self):
        """增加章节评论"""
        data = {
            "content": "",
            "book_id": "",
            "chapter_id": "",
            "cmd_id": "",
            "author_id": "",
            "comment_id": ""
        }
        res = requests.post(url=base_url + "/app/chapter/add-chapter-comment", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_comment_praise_cancel(self):
        """点赞评论"""
        data = {
            "book_id": "",
            "comment_id": "",
            "author_id": "",
            "chapter_id": "",
            "cmd_id": ""
        }
        res = requests.post(url=base_url + "/app/chapter/comment-praise-cancel", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_comment_praise(self):
        """取赞评论"""
        data = {
            "book_id": "",
            "comment_id": "",
            "author_id": "",
            "chapter_id": "",
            "cmd_id": ""
        }
        res = requests.post(url=base_url + "/app/chapter/comment-praise", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_comment_reply_list(self):
        """获取评论回复列表"""
        data = {
            "book_id": "",
            "chapter_id": "",
            "cmd_id": "",
            "id": "",
            "page_num": ""
        }
        res = requests.post(url=base_url + "/app/chapter/comment-reply-list", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_comment_reply_add(self):
        """增加评论回复"""
        data = {
            "content": "",
            "book_id": "",
            "chapter_id": "",
            "cmd_id": "",
            "author_id": "",
            "comment_id": ""
        }
        res = requests.post(url=base_url + "/app/chapter/comment-reply-add", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_comment_reply_del(self):
        """删除评论回复"""
        data = {
            "book_id": "",
            "comment_id": "",
            "cmd_id": "",
            "comment_reply_id": ""
        }
        res = requests.post(url=base_url + "/app/chapter/comment-reply-del", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_comment_reply_praise(self):
        """点赞回复"""
        data = {
            "comment_reply_id": "",
            "author_id": "",
            "book_id": "",
            "chapter_id": "",
            "cmd_id": ""
        }
        res = requests.post(url=base_url + "/app/chapter/comment-reply-praise", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_comment_reply_praise_list(self):
        """取赞回复"""
        data = {
            "comment_reply_id": "",
            "author_id": "",
            "book_id": "",
            "chapter_id": "",
            "cmd_id": ""
        }
        res = requests.post(url=base_url + "/app/chapter/comment-reply-praise-cancel", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_comment_count(self):
        """根据对话体ID获取 评论总数 点赞总数"""
        data = {
            "book_id": "",
            "chapter_id": "",
            "cmd_ids": ""
        }
        res = requests.post(url=base_url + "/app/chapter/comment-count", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_face(self):
        """表情态度"""
        data = {
            "face_id": "",
            "author_id": "",
            "book_id": "",
            "chapter_id": "",
            "cmd_id": ""
        }
        res = requests.post(url=base_url + "/app/chapter/face", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
