from tool.get_token import *


class MyTestCase(unittest.TestCase):
    """编辑器"""

    def setUp(self):
        self.page_num = 1
        self.page_size = 5

    def test_cates(self):
        """获取分类"""
        res = requests.post(url=base_url + "/app/editor/cates",headers=headers)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_books(self):
        """书本列表"""
        data = {
            "sort": -1,
            "sort_type": 0,
            "audit_status": -1,
            "page_num": self.page_num,
            "page_size": self.page_size
        }
        res = requests.post(url=base_url + "/app/editor/books", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_add_book(self):
        """添加书本"""
        data = {
            "name": "python创建书本",
            "desc": "窝窝头，一块钱四个，嘿嘿！",
            "image": "",
            "cate": [],
            "work_status": 0,
            "cate_id": ""
        }
        res = requests.post(url=base_url + "/app/editor/add-book", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_del_book(self):
        """删除书本"""
        data = {
            "book_id": self.test_add_book()
        }
        res = requests.post(url=base_url + "/app/editor/del-book", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def test_(self):
        """"""
        data = {
            "": "",
            "": "",
            "": "",
            "": ""
        }
        res = requests.post(url=base_url + "", headers=headers, json=data)
        print(res.text)
        self.assertTrue(u"success" in res.text)

    def tearDown(self):
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()
