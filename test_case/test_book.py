from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """评论书本"""

    def setUp(self):
        # 70648311677614-怎么办！那个女孩的毛发太旺盛！
        self.book_id = 70648311677614
        self.page_num = 1
        self.page_size = 5
        # 10004-钱过敏
        self.user_id = 10004

    def test_h5_file(self):
        """获取 book H5"""
        data = {
            "book_id": self.book_id
        }
        res = requests.post(url= base_url + "/app/book/h5-file",headers=headers,json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_book_file(self):
        """获取播放文件"""
        data = {
            "book_id": self.book_id
        }
        res = requests.post(url=base_url + "/app/book/book-file", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_list(self):
        """获取首页书本列表"""
        data = {
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/book/list", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_list_tag(self):
        """获取标签书本列表"""
        data = {
            "page_num": self.page_num,
            "page_size": self.page_size,
            "cate_id": 2,
            "order": 0
        }
        res = requests.post(url=base_url + "/app/book/list-tag", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_books_by_class(self):
        """获取专栏书本列表"""
        data = {
            "page_num": self.page_num,
            "page_size": self.page_size,
            "cate_id": 2
        }
        res = requests.post(url=base_url + "/app/book/get-books-by-class", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_recommends(self):
        """获取推荐作品列表"""
        data = {
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/book/recommends", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_collect_list(self):
        """获取书本收藏列表"""
        data = {
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/book/collect-list", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_history_list(self):
        """获取书本浏览记录"""
        data = {
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/book/history-list", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_collect(self):
        """收藏书本"""
        data = {
            "book_id": self.book_id,
            "type": 0
        }
        res = requests.post(url=base_url + "/app/book/collect", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_collect1(self):
        """取消收藏书本"""
        data = {
            "book_id": self.book_id,
            "type": 1
        }
        res = requests.post(url=base_url + "/app/book/collect", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_praise(self):
        """点赞书本"""
        data = {
            "book_id": self.book_id,
            "author_id": self.user_id
        }
        res = requests.post(url=base_url + "/app/book/praise", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_praise_cancel(self):
        """取赞书本"""
        data = {
            "book_id": self.book_id,
            "author_id": self.user_id
        }
        res = requests.post(url=base_url + "/app/book/praise-cancel", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_get_book(self):
        """作品详情"""
        data = {
            "book_id": self.book_id,
            "author_id": self.user_id
        }
        res = requests.post(url=base_url + "/app/book/get-book", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_share(self):
        """分享上报"""
        data = {
            "book_id": self.book_id
        }
        res = requests.post(url=base_url + "/app/book/share", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_list_activity(self):
        """获取活动相关书本列表"""
        data = {
            "activity_id": 130608457596928,
            "user_id": self.user_id,
            "order": 1, # 0是最新1是最热排序
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/book/list-activity", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_search_book(self):
        """搜索书本"""
        data = {
            "keyword": "相见",
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/book/search-book", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
